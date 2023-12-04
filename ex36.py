to_do_list = [
    "calculate the area of a rectangle",
    "to generate Fibonacci sequence",
    "Implement a simple shopping cart functionality",
]

easiest_task = to_do_list[0]

if easiest_task == "calculate the area of a rectangle":
    
    def calculate_rectangle_area(length, width):
        area = length * width
        return area

    length = 5
    width = 10
    calculated_area = calculate_rectangle_area(length, width)
    print(f"Area of rectangle with length {length} and width {width} is: {calculated_area}")
