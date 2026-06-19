import json
from uuid import uuid4

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
from gi.repository import Gdk, GLib, Gtk


class BoardModel:
    def __init__(self):
        self.columns = {
            "TODO": [
                {
                    "id": str(uuid4()),
                    "title": "Learn GTK",
                    "type": "learning",
                    "priority": "high",
                    "description": "Read the docs and build a small draggable board.",
                    "subtasks": [
                        {"title": "Install GTK4 bindings", "status": "done"},
                        {
                            "title": "Understand widgets and containers",
                            "status": "progress",
                        },
                        {"title": "Practice drag and drop", "status": "todo"},
                    ],
                },
                {
                    "id": str(uuid4()),
                    "title": "Learn CSS",
                    "type": "learning",
                    "priority": "medium",
                    "description": "Style the board with simple GTK CSS.",
                    "subtasks": [
                        {"title": "Study selectors", "status": "done"},
                        {"title": "Try spacing and padding", "status": "todo"},
                    ],
                },
            ],
            "DOING": [
                {
                    "id": str(uuid4()),
                    "title": "Improve Kanban UI",
                    "type": "feature",
                    "priority": "high",
                    "description": "Add metadata to cards and make them easier to scan.",
                    "subtasks": [
                        {"title": "Show type and priority", "status": "done"},
                        {
                            "title": "Show subtask progress",
                            "status": "progress",
                        },
                        {"title": "Polish card layout", "status": "todo"},
                    ],
                }
            ],
            "DONE": [],
        }

    def find_task_location(self, task_id):
        for column_name, tasks in self.columns.items():
            for index, task in enumerate(tasks):
                if task["id"] == task_id:
                    return column_name, index, task
        return None, None, None

    def move_task(self, task_id, target_column):
        source_column, index, task = self.find_task_location(task_id)
        if task is None or source_column == target_column:
            return False

        self.columns[source_column].pop(index)
        self.columns[target_column].append(task)
        return True


def clear_container(container):
    child = container.get_first_child()
    while child:
        next_child = child.get_next_sibling()
        container.remove(child)
        child = next_child


def make_badge(text, style_class=None):
    label = Gtk.Label(label=text)
    label.set_xalign(0)

    # turn label into "pill"
    label.add_css_class("badge")
    if style_class:
        label.add_css_class(style_class)

    return label


def subtasks_summary(task):
    subtasks = task.get("subtasks", [])
    if not subtasks:
        return "0/0"

    done = sum(1 for s in subtasks if s.get("status") == "done")
    total = len(subtasks)
    return f"{done}/{total}"


def create_task_card(task, source_column):
    container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
    container.set_margin_top(8)
    container.set_margin_bottom(8)
    container.set_margin_start(8)
    container.set_margin_end(8)

    # ---------------- TITLE ----------------
    title = Gtk.Label()
    title.set_xalign(0)
    title.set_wrap(True)
    title.set_markup(f"<b>{GLib.markup_escape_text(task['title'])}</b>")
    container.append(title)

    # ---------------- DESCRIPTION ----------------
    description = task.get("description", "")
    if description:
        desc = Gtk.Label(label=description)
        desc.set_xalign(0)
        desc.set_wrap(True)
        desc.add_css_class("muted")
        container.append(desc)

    # ---------------- FOOTER (BADGES) ----------------
    footer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    footer.set_margin_top(6)

    # TYPE badge
    footer.append(
        make_badge(task.get("type", "unknown").upper(), "badge-type")
    )

    # PRIORITY badge (styled by level)
    priority = task.get("priority", "low")
    footer.append(make_badge(priority.upper(), f"badge-priority-{priority}"))

    # SUBTASK PROGRESS badge
    footer.append(
        make_badge(f"SUB {subtasks_summary(task)}", "badge-subtasks")
    )

    container.append(footer)

    # ---------------- DRAG WRAPPER ----------------
    button = Gtk.Button()
    button.set_child(container)

    drag_source = Gtk.DragSource.new()
    drag_source.set_actions(Gdk.DragAction.MOVE)

    def prepare_drag(source, x, y):
        payload = json.dumps(
            {
                "source": source_column,
                "task_id": task["id"],
            }
        )
        return Gdk.ContentProvider.new_for_value(payload)

    drag_source.connect("prepare", prepare_drag)
    button.add_controller(drag_source)

    return button


def on_drop(drop_target, value, x, y, target_col_name, model, board_box):
    if isinstance(value, GLib.Variant):
        data_str = value.get_string()
    else:
        data_str = str(value)

    try:
        payload = json.loads(data_str)
    except json.JSONDecodeError:
        return False

    task_id = payload.get("task_id")
    if not task_id:
        return False

    moved = model.move_task(task_id, target_col_name)
    if moved:
        build_board(board_box, model)
    return moved


def build_board(board_box, model):
    clear_container(board_box)

    for col_name, tasks in model.columns.items():
        column_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        column_box.set_margin_top(6)
        column_box.set_margin_bottom(6)
        column_box.set_margin_start(6)
        column_box.set_margin_end(6)

        header = Gtk.Label(label=col_name)
        header.set_xalign(0)
        header.set_markup(f"<b>{GLib.markup_escape_text(col_name)}</b>")
        column_box.append(header)

        drop_target = Gtk.DropTarget.new(str, Gdk.DragAction.MOVE)
        drop_target.connect("drop", on_drop, col_name, model, board_box)
        column_box.add_controller(drop_target)

        for task in tasks:
            card = create_task_card(task, col_name)
            column_box.append(card)

        frame = Gtk.Frame()
        frame.set_child(column_box)
        frame.set_hexpand(True)
        frame.set_vexpand(True)
        board_box.append(frame)


class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyKanbanApp")
        GLib.set_application_name("My Kanban App")
        self.model = BoardModel()

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Kanban Board")
        window.set_default_size(1100, 700)

        # style css
        css = b"""
.badge {
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 11px;
    background: #2b2b2b;
    color: white;
}

.badge-type {
    background: #3a6ea5;
}

.badge-priority-high {
    background: #d64545;
}

.badge-priority-medium {
    background: #d6a545;
}

.badge-priority-low {
    background: #4caf50;
}

.badge-subtasks {
    background: #555;
}

.muted {
    opacity: 0.7;
    font-size: 11px;
}
"""

        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        main_box.set_margin_top(12)
        main_box.set_margin_bottom(12)
        main_box.set_margin_start(12)
        main_box.set_margin_end(12)
        window.set_child(main_box)

        title = Gtk.Label(label="My Board")
        title.set_halign(Gtk.Align.CENTER)
        title.set_markup("<b>My Board</b>")
        main_box.append(title)

        board = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        board.set_hexpand(True)
        board.set_vexpand(True)
        main_box.append(board)

        build_board(board, self.model)

        window.present()


app = MyApplication()
app.run()
