from tkinter import *

app=Tk()
app.title("my first pythonprog using cars in gui app")
app.geometry("500x500+500+100")
app.config(bg="white")

def clickresult():
    details="tata cars are safe and secure for a family drive "
    lblTitle.config(text=details, fg="red")


lblTitle=Label(app,text="Brand Name")
lblTitle.grid(row=0, column=1, padx=40, pady=40)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=0, column=2)


lblTitle1=Label(app,text="Car Name")
lblTitle1.grid(row=1, column=1, padx=40, pady=40)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=1, column=2)


clickme=Button(app, text="details for given car", command=clickresult, )
clickme.grid(row=2, column=8, padx=40, pady=40)


app.mainloop()

'''import tkinter as tk

def calculate():
    # Perform some calculation
    result = 10 + 5  # Example calculation

    # Create a new window to display the result
    result_window = tk.Toplevel(root)
    result_window.title("Result")

    # Display the result in a label
    result_label = tk.Label(result_window, text=f"Result: {result}")
    result_label.pack()

# Create the main window
root = tk.Tk()
root.title("Result Button")

# Create and pack widgets
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Start the event loop
root.mainloop()'''