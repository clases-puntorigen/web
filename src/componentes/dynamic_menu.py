from nicegui import ui

class DynamicMenu:
    def __init__(self, menu, on_item_click, 
                 header_classes="bg-primary text-white text-bold", 
                 item_classes="bg-white text-black"):
        """
        Initialize the DynamicMenu component.

        :param menu: List of menu items (strings, lists, or callables with docstrings).
        :param on_item_click: Function to call when a menu item is clicked.
        :param header_classes: Optional classes to apply to headers (expansion titles and labels).
        :param item_classes: Optional classes to apply to clickable items (default: "bg-white text-black").
        """
        self.menu = menu 
        self.on_item_click = on_item_click
        self.header_classes = header_classes
        self.item_classes = item_classes
        self._render_menu()

    def _render_menu(self):
        """
        Automatically render the dynamic menu on initialization.

        :return: None
        """
        with ui.list().props("bordered separator").classes("w-full"):
            for item in self.menu:
                self._render_item(item)

    def _render_item(self, item):
        """
        Render an individual menu item.

        :param item: Menu item (string, list, or callable).
        :return: None
        """
        if isinstance(item, list):
            self._render_expansion(item)
        elif isinstance(item, str):
            if item == "---":
                ui.separator()
            else:
                self._render_label(item)
        else:
            self._render_callable_item(item)

    def _render_expansion(self, item):
        """
        Render an expandable menu item.

        :param item: List of items to be included in the expansion.
        :return: None
        """
        with ui.expansion(item[0]).props(f'header-class="{self.header_classes}"').classes('w-full uppercase'):
            with ui.list().props("bordered separator").classes("w-full"):
                for sub_item in item[1:]:
                    self._render_item(sub_item)

    def _render_label(self, label):
        """
        Render a simple label item.

        :param label: Label text.
        :return: None
        """
        with ui.item_section():
            ui.item_label(label.upper()).props("header").classes(self.header_classes)
        ui.separator()

    def _render_callable_item(self, item):
        """
        Render a menu item that is a callable.

        :param item: Callable item with a docstring.
        :return: None
        """
        title = item.__doc__ or "Untitled"
        icon = None
        caption = None

        # Extract icon and title from the docstring
        if title.startswith("[") and "]" in title:
            icon = title[1:title.index("]")]
            title = title[title.index("]") + 1:].strip()

        # Split title and caption if ':' exists
        if ":" in title:
            title, caption = title.split(":", 1)
            title = title.strip()
            caption = caption.strip()

        with ui.item(on_click=lambda: self.on_item_click(item)).classes(f"w-full {self.item_classes}"):
            if icon:
                with ui.item_section().props('side'):
                    ui.icon(icon)
            with ui.item_section():
                ui.item_label(title).classes("normal-case w-full")
                if caption:
                    ui.item_label(caption).props("caption")
