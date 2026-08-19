# GTK4 app development

## Resources:

- https://pygobject.gnome.org/tutorials/index.html
- https://developer.gnome.org/documentation/tutorials/beginners/getting_started.html

## Tools:

- gnome builder is necassary to create for gnome app which include flatpak manifest etc. when create project.
- if you need designer tool glade ceased on 2022 and below is the up-to-date new tool for designing gtk3/gtk4 ui:
  - https://flathub.org/en/apps/ar.xjuan.Cambalache

## What project that I use to learn?

- Kanban app that handle projects
- Use markdown files to handle todos instead of any other database which database often cause issues and also user don't need to use my app all the time, time passes and new app can be better for them and they can get their markdown file and switch to new app without any issue because all of their tasks is markdown.

- How the ui would look like and what are the important stuff?
  - need to be a list for projects to select
  - need a button the create project
  - need a button to rename/delete/add new kanban columns
  - need a button to add tasks to columns
  - need a good card layout for tasks
  - need to show priority, type on tasks (bug, p1)
  - need a button to add subtasks to tasks card

I want to make kanban app that use markdown file as a database like headings are going to be label for tasks like ## todo, ## doing and checkboxes are tasks and than #id-asdg1341 8-hex is going to be work for handling sorting etc., and yaml frontmatter on that project md file going to be handle the sorting for each column sorting manually, but I also need description for each task below - this seems hard for me but I though I could find a way to handle it - , python is going to be used on this project with pygobject gtk.
