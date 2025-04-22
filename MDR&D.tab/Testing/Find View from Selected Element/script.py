from pyrevit import forms
from pyrevit import revit, DB

# Assuming you have selected an element in Revit
selected_element_ids = rvt.uidoc.selection.GetElementIds()
if selected_element_ids:
    element_id = selected_element_ids[0]
    element = rvt.doc.GetElement(element_id)

    # Access the element's VisibleIn property
    view_ids = element.VisibleIn

    if view_ids:
        print("Element is visible in the following view IDs:")
        for view_id in view_ids:
            view = rvt.doc.GetElement(view_id)
            print(f"{view.Name} ({view_id})")
    else:
        print("Element is not visible in any view.")
else:
    print("No element selected.")
