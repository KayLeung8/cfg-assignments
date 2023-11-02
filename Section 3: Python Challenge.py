def minimum_classes(students):
    if students <= 30:
        allocation = {'Class 1': students // 2, 'Class 2': students - students // 2}
        return f"Proposed Allocation: 2 classes\nAllocation: {allocation}"
    
    num_classes = (students + 29) // 30
    per_class = students // num_classes
    extra_students = students % num_classes

    allocation = {}
    for i in range(num_classes):
        class_name = f"Class {i+1}"
        if i < extra_students:
            allocation[class_name] = per_class + 1
        else:
            allocation[class_name] = per_class

    return f"Proposed Allocation: {num_classes} classes\nAllocation: {allocation}"

# Test
print(minimum_classes(31))
print(minimum_classes(59))
print(minimum_classes(87))
