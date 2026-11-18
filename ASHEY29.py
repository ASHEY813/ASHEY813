import tkinter as tk
import math
import random

# ==========================================
#       PYTHON DISCOVERY CENTER
# ==========================================

def show_lessons():

    print("=" * 55)
    print("          PYTHON DISCOVERY CENTER")
    print("       EXPLORE THE WORLD OF CODING")
    print("=" * 55)

    print("\nWELCOME, FUTURE PROGRAMMER!")

    name = input("\nEnter your name: ")

    print("\nHello,", name + "!")
    print("Let's begin your coding adventure!")

    while True:

        print("\n" + "=" * 55)
        print("             AVAILABLE LESSONS")
        print("=" * 55)

        print("1. What is Programming?")
        print("2. Understanding Variables")
        print("3. Python Data Types")
        print("4. Mathematical Operations")
        print("5. Getting User Information")
        print("6. Making Decisions")
        print("7. Repeating Instructions")
        print("8. Exit Lessons")

        print("=" * 55)

        choice = input("\nChoose your lesson (1-8): ")

        if choice == "1":
            print("\nLESSON 1: WHAT IS PROGRAMMING?")
            print("Programming means giving instructions")
            print("to a computer to perform tasks.")

        elif choice == "2":
            print("\nLESSON 2: UNDERSTANDING VARIABLES")
            print("Variables store information.")
            print("Example:")
            print("student = 'Alex'")
            print("print(student)")

        elif choice == "3":
            print("\nLESSON 3: PYTHON DATA TYPES")
            print("String - Text")
            print("Integer - Whole numbers")
            print("Float - Decimal numbers")
            print("Boolean - True or False")

        elif choice == "4":
            print("\nLESSON 4: MATHEMATICAL OPERATIONS")
            print("x = 20")
            print("y = 10")
            print("print(x + y)")
            print("print(x - y)")
            print("print(x * y)")
            print("print(x / y)")

        elif choice == "5":
            print("\nLESSON 5: GETTING USER INFORMATION")
            print("city = input('Enter your city: ')")
            print("print('Your city is', city)")

        elif choice == "6":
            print("\nLESSON 6: MAKING DECISIONS")
            print("score = 90")
            print("if score >= 75:")
            print("    print('Passed')")
            print("else:")
            print("    print('Failed')")

        elif choice == "7":
            print("\nLESSON 7: REPEATING INSTRUCTIONS")
            print("for i in range(5):")
            print("    print('Keep Learning!')")

        elif choice == "8":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\nInvalid choice! Select 1 to 8.")

        input("\nPress ENTER to continue...")


# ==========================================
#       THE WHOLE LIFE OF A FLOWER
# ==========================================

def open_flower():

    WIDTH = 800
    HEIGHT = 600

    root = tk.Tk()
    root.title("The Whole Life of a Flower")
    root.resizable(False, False)

    canvas = tk.Canvas(
        root,
        width=WIDTH,
        height=HEIGHT,
        bg="#080817",
        highlightthickness=0
    )
    canvas.pack()

    frame = 0
    stars = []

    for i in range(65):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 100)
        size = random.randint(1, 3)
        stars.append((x, y, size))

    def glow_circle(x, y, radius, color):

        for extra in range(8, 0, -2):
            canvas.create_oval(
                x-radius-extra,
                y-radius-extra,
                x+radius+extra,
                y+radius+extra,
                fill="",
                outline=color,
                width=2
            )

        canvas.create_oval(
            x-radius, y-radius,
            x+radius, y+radius,
            fill=color,
            outline=color
        )

    def draw_flower():

        nonlocal frame

        canvas.delete("all")

        canvas.create_rectangle(
            0, 0, WIDTH, HEIGHT,
            fill="#080817",
            outline=""
        )

        for x, y, size in stars:
            canvas.create_oval(
                x, y, x+size, y+size,
                fill="#7777aa",
                outline=""
            )

        canvas.create_line(
            0, 510, WIDTH, 510,
            fill="#30304b",
            width=3
        )

        canvas.create_text(
            WIDTH//2, 35,
            text="THE WHOLE LIFE OF A FLOWER",
            fill="white",
            font=("Arial", 20, "bold")
        )

        canvas.create_text(
            WIDTH//2, 65,
            text="A little seed, a beautiful journey",
            fill="#ff9de2",
            font=("Arial", 11)
        )

        center_x = WIDTH // 2
        ground_y = 505

        stage = (frame // 100) % 6
        progress = (frame % 100) / 100

        if stage == 0:

            glow_circle(
                center_x, ground_y-8, 5, "#d6a45c"
            )

            message = "DAY 01 - A tiny seed"

        elif stage == 1:

            height = progress * 100

            canvas.create_line(
                center_x, ground_y,
                center_x, ground_y-height,
                fill="#42ffb0",
                width=5
            )

            glow_circle(
                center_x,
                ground_y-height,
                5,
                "#8affd0"
            )

            message = "DAY 10 - A little sprout"

        elif stage == 2:

            height = 100 + progress * 150
            top = ground_y - height

            canvas.create_line(
                center_x, ground_y,
                center_x, top,
                fill="#42ffb0",
                width=6
            )

            for side in [-1, 1]:

                leaf_y = ground_y - height * 0.55

                canvas.create_oval(
                    center_x-side*65-25,
                    leaf_y-10,
                    center_x-side*5+25,
                    leaf_y+20,
                    fill="#24c98a",
                    outline="#8affc8",
                    width=2
                )

            glow_circle(center_x, top, 7, "#a5ffe0")

            message = "DAY 20 - Growing stronger"

        elif stage == 3 or stage == 4:

            height = 260
            top = ground_y - height

            canvas.create_line(
                center_x, ground_y,
                center_x, top,
                fill="#42ffb0",
                width=7
            )

            for side in [-1, 1]:

                leaf_y = ground_y - 120

                canvas.create_oval(
                    center_x-70 if side == -1 else center_x+5,
                    leaf_y-15,
                    center_x-5 if side == -1 else center_x+70,
                    leaf_y+15,
                    fill="#20c987",
                    outline="#8affc8",
                    width=2
                )

            petal_size = 12 + progress * 15

            for angle in range(0, 360, 45):

                radians = math.radians(angle)

                px = center_x + math.cos(radians)*35
                py = top + math.sin(radians)*35

                canvas.create_oval(
                    px-petal_size,
                    py-petal_size,
                    px+petal_size,
                    py+petal_size,
                    fill="#ff75dc",
                    outline="#ffc5f2",
                    width=2
                )

            glow_circle(center_x, top, 13, "#fff18a")

            message = "DAY 30 - The flower is blooming"

        else:

            top = ground_y - 210

            canvas.create_line(
                center_x, ground_y,
                center_x+25, top,
                fill="#91a66b",
                width=6
            )

            for angle in range(0, 360, 60):

                radians = math.radians(angle)

                px = center_x+25 + math.cos(radians)*25
                py = top + math.sin(radians)*18

                canvas.create_oval(
                    px-10, py-10,
                    px+10, py+10,
                    fill="#b58a75",
                    outline="#d5b49b"
                )

            glow_circle(
                center_x+25, top, 7, "#e6c78c"
            )

            message = "DAY 50 - The flower rests"

        canvas.create_text(
            WIDTH//2, 555,
            text=message,
            fill="#ffffff",
            font=("Arial", 15, "bold")
        )

        frame += 1

        root.after(50, draw_flower)

    draw_flower()
    root.mainloop()


# ==========================================
#             MAIN MENU
# ==========================================

def main_menu():

    while True:

        print("\n" + "=" * 55)
        print("          PYTHON DISCOVERY CENTER")
        print("=" * 55)

        print("\nWELCOME TO THE CODING HUB!")
        print("\n1. Explore Python Lessons")
        print("2. Watch Flower Life Animation")
        print("3. Exit Program")

        print("=" * 55)

        choice = input("\nChoose an option (1-3): ")

        if choice == "1":

            show_lessons()

        elif choice == "2":

            print("\nOpening Flower Animation...")
            open_flower()

        elif choice == "3":

            print("\nThank you for visiting!")
            print("Keep exploring and never stop learning!")
            print("GOODBYE!")
            break

        else:

            print("\nInvalid choice! Please select 1 to 3.")


# START PROGRAM
main_menu()

#What I Learned from the Python Code

#1. Programming – I learned that programming means giving instructions to a computer to perform different tasks.

#2. Variables – I learned how to store information using variables.

#3. Data Types – I learned the different data types, such as String, Integer, Float, and Boolean.

#4. Mathematical Operations – I learned how to use addition, subtraction, multiplication, and division in Python.

#5. User Input – I learned how to get information from users using input().

#6. Conditional Statements – I learned how to use if and else to make decisions.

#7. Loops – I learned how to repeat instructions using for and while loops.

#8. Tkinter – I learned how to create a graphical interface using Tkinter.

#9. Canvas Drawing – I learned how to draw shapes, lines, circles, and text on the screen.

#10. Animation – I learned how to use random and frame to create stars and flower animations.

#Overall Learning:

# I learned that Python is not only used for simple programs but also for creating interactive lessons, drawings, and animations.
#This activity helped me understand coding better and improve my programming skills.