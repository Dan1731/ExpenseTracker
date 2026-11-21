/// This file controls the action dropdown menu inside the expense table. It allows the three-dot dropdown to open and close
/// when the user clicks the button or somewhere outside of the action menu.

/// For each expense line.
document.querySelectorAll(".action-button").forEach(button => {
    button.addEventListener("click", () => {
        const menu = button.nextElementSibling;

        /// For each dropdown menu.
        document.querySelectorAll(".action-menu").forEach(otherMenu => {
            /// If the menu is not the action menu the user selected, then the menu does not display.
            /// Prevents all expense menus from popping up when the user selects an action.
            if (otherMenu !== menu) {
                otherMenu.hidden = true;
            }
        });

        // Toggle the selected menu open or closed.
        menu.hidden = !menu.hidden;
    });
});

// Close menus when clicking outside.
document.addEventListener("click", event => {
    if (!event.target.closest(".action-class")) {
        document.querySelectorAll(".action-menu").forEach(menu => {
            menu.hidden = true;
        });
    }
});