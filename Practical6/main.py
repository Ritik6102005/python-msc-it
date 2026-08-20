from Students_data import get_student_data
from sort import sort_marks
from Students_rank import rank_marks
from display import display

std_data = get_student_data()
sort_data = sort_marks(std_data)
rank_data = rank_marks(sort_data)
display_data = display(rank_data)
print(display_data)