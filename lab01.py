
from math import floor



total_bw = 33
channel_bw = 25*2
total_available_channel = 33000/50
print("total_available_channel", total_available_channel)
available_control_channel = 1000/channel_bw
print("available_control_channel", available_control_channel)

#for N = 4

print("(a)")
total_No_Of_available_channel_per_cell_for_four_cell_reuse = floor(total_available_channel/4)
print("total_No_Of_available_channel_per_cell_for_four_cell_reuse", total_No_Of_available_channel_per_cell_for_four_cell_reuse)

number_Of_voice_channel_for_four_cell_reuse = floor((total_available_channel - available_control_channel)/4)
print("number_Of_voice_channel_for_four_cell_reuse", number_Of_voice_channel_for_four_cell_reuse)

number_Of_control_channel_for_four_cell_reuse= total_No_Of_available_channel_per_cell_for_four_cell_reuse - number_Of_voice_channel_for_four_cell_reuse
print("number_Of_control_channel_for_four_cell_reuse",number_Of_control_channel_for_four_cell_reuse)

#for N = 7

print("(b)")
total_No_Of_available_channel_per_cell_for_seven_cell_reuse =floor(total_available_channel/7)
print("total_No_Of_available_channel_per_cell_for_seven_cell_reuse", total_No_Of_available_channel_per_cell_for_seven_cell_reuse)

number_Of_voice_channel_for_seven_cell_reuse = floor((total_available_channel - available_control_channel)/7)
print("number_Of_voice_channel_for_seven_cell_reuse", number_Of_voice_channel_for_seven_cell_reuse)

number_Of_control_channel_for_seven_cell_reuse= total_No_Of_available_channel_per_cell_for_seven_cell_reuse - number_Of_voice_channel_for_seven_cell_reuse
print("number_Of_control_channel_for_seven_cell_reuse", number_Of_control_channel_for_seven_cell_reuse)

#for N = 12

print("(c)")
total_No_Of_available_channel_per_cell_for_twelve_cell_reuse =floor(total_available_channel/12)
print("total_No_Of_available_channel_per_cell_for_twelve_cell_reuse", total_No_Of_available_channel_per_cell_for_twelve_cell_reuse)

number_Of_voice_channel_for_twelve_cell_reuse = floor((total_available_channel - available_control_channel)/12)
print("number_Of_voice_channel_for_twelve_cell_reuse", number_Of_voice_channel_for_twelve_cell_reuse)

number_Of_control_channel_for_twelve_cell_reuse= total_No_Of_available_channel_per_cell_for_twelve_cell_reuse - number_Of_voice_channel_for_twelve_cell_reuse
print("number_Of_control_channel_for_twelve_cell_reuse",number_Of_control_channel_for_twelve_cell_reuse)