import json

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
from gi.repository import Gdk, GLib, Gtk


class BoardModel:
    def __init__(self):
        self.columns = {
            "TODO": ["Learn GTK", "Learn CSS"],
            "DOING": [],
            "DONE": [],
        }


def on_drag_prepare(drag_source, x, y, card_text, source_column):
    data = f"{source_column}::{card_text}"
    return Gdk.ContentProvider.new_for_value(data)


def on_drop(drop_target, value, x, y, target_col_name, model, board_box):
    data_str = value

    if isinstance(value, GLib.Variant):
        data_str = value.get_string()
    else:
        data_str = str(value)

    try:
        payload = json.loads(data_str)
    except json.JSONDecodeError:
        return False

    source_col = payload["source"]
    card_text = payload["text"]

    if source_col == target_col_name:
        return False

    model.columns[source_col].remove(card_text)
    model.columns[target_col_name].append(card_text)

    GLib.idle_add(build_board, board_box, model)
    return True


def create_card(text, source_column):
    card = Gtk.Button(label=text)

    drag_source = Gtk.DragSource.new()
    drag_source.set_actions(Gdk.DragAction.MOVE)

    def prepare_drag(source, x, y):
        data = json.dumps({"source": source_column, "text": text})
        return Gdk.ContentProvider.new_for_value(data)

    drag_source.connect("prepare", prepare_drag)
    card.add_controller(drag_source)

    return card


def build_board(board_box, model):
    # remove all columns (assumes board_box only contains frames)
    clear_container(board_box)

    for col_name, cards in model.columns.items():
        column_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        column_box.append(Gtk.Label(label=col_name))

        drop_target = Gtk.DropTarget.new(str, Gdk.DragAction.MOVE)
        drop_target.connect("drop", on_drop, col_name, model, board_box)
        column_box.add_controller(drop_target)

        # Add cards
        for card_text in cards:
            card = create_card(card_text, col_name)
            column_box.append(card)

        frame = Gtk.Frame()
        frame.set_child(column_box)
        frame.set_hexpand(True)
        board_box.append(frame)


def clear_container(container):
    child = container.get_first_child()
    while child:
        next_child = child.get_next_sibling()
        container.remove(child)
        child = next_child


class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyKanbanApp")
        GLib.set_application_name("My Kanban App")
        self.model = BoardModel()  # our in‑memory model

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Kanban Board")
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        window.set_child(main_box)

        title = Gtk.Label(label="My Board")
        title.set_halign(Gtk.Align.CENTER)
        main_box.append(title)

        # The board will hold the three columns
        board = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        board.set_hexpand(True)
        board.set_vexpand(True)
        main_box.append(board)

        # Build the board once from the model
        build_board(board, self.model)

        window.present()


app = MyApplication()
app.run()
