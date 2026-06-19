import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk


class MyApplication(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name("My Kanban App")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Kanban Board")

        # main vertical box to hold title and board
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # add the board to the window
        window.set_child(main_box)

        # title label
        title = Gtk.Label(label="My Board")
        title.set_halign(Gtk.Align.CENTER)
        main_box.append(title)

        # horizontal board layout
        board = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        board.set_hexpand(True)
        board.set_vexpand(True)
        main_box.append(board)

        # create the three todo,doing,done columns
        todo_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        doing_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        done_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # define todo columen titles
        todo_column.append(Gtk.Label(label="TODO"))
        doing_column.append(Gtk.Label(label="DOING"))
        done_column.append(Gtk.Label(label="DONE"))

        # add cards
        todo_column.append(create_card("Learn GTK"))
        todo_column.append(create_card("Learn CSS"))

        # # each column gets equel width
        # +------+ +------+ +------+
        # | TODO | |DOING | | DONE |
        # +------+ +------+ +------+
        todo_frame = Gtk.Frame()
        todo_frame.set_child(todo_column)
        todo_frame.set_hexpand(True)

        doing_frame = Gtk.Frame()
        doing_frame.set_child(doing_column)
        doing_frame.set_hexpand(True)

        done_frame = Gtk.Frame()
        done_frame.set_child(done_column)
        done_frame.set_hexpand(True)

        # add the frames to the board
        board.append(todo_frame)
        board.append(doing_frame)
        board.append(done_frame)

        window.present()


def create_card(text):
    card = Gtk.Button(label=text)
    card.set_margin_top(4)
    card.set_margin_bottom(4)
    return card


app = MyApplication()
app.run()
