from tkinter import *
from datetime import *

root = Tk()
root.title(f"{datetime.now():%a, %b %d %Y} | Pool.io ")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("+%d+%d" % (300, 100))




def add_joints():

    #-------------Joints------------------
    top = Toplevel()
    top.geometry("+%d+%d" % (300, 100))

    # tj_label = Label(top, text="Tee Joint", fg="blue")
    # tj_label.grid(row=0, column=0, padx=10, pady=10)

    tj_label = Label(top, text="Tee Joint Diameter:")
    tj_label.grid(row=1, column=0, padx=10, pady=10)
    tj_list = ["152.4 mm", "203.2 mm", "254 mm", "304.8 mm", "355.6 mm", "406.4 mm"]
    clicked_tj = StringVar(top)
    clicked_tj.set(tj_list[0])
    drop = OptionMenu(top, clicked_tj, *tj_list)
    drop.grid(row=1, column=1)

    ninety_label = Label(top, text="90° Elbow ")
    ninety_label.grid(row=2, column=0, padx=10, pady=10)

    ninety_list = ["152.4 mm", "203.2 mm", "254 mm", "304.8 mm", "355.6 mm", "406.4 mm"] 
    clicked_ninety = StringVar(top)
    clicked_ninety.set(ninety_list[0])
    drop = OptionMenu(top, clicked_ninety, *ninety_list)
    drop.grid(row=2, column=1)


    lre_label = Label(top, text="Long Radius Elbow ")
    lre_label.grid(row=3, column=0, padx=10, pady=10)

    lre_list = ["152.4 mm", "203.2 mm", "254 mm", "304.8 mm", "355.6 mm", "406.4 mm"] 
    clicked_lre = StringVar(top)
    clicked_lre.set(lre_list[0])
    drop = OptionMenu(top, clicked_lre, *lre_list)
    drop.grid(row=3, column=1)

    forty_label = Label(top, text="45° Elbow Elbow ")
    forty_label.grid(row=4, column=0, padx=10, pady=10)

    forty_list = ["152.4 mm", "203.2 mm", "254 mm", "304.8 mm", "355.6 mm", "406.4 mm"] 
    clicked_forty = StringVar(top)
    clicked_forty.set(forty_list[0])
    drop = OptionMenu(top, clicked_forty, *forty_list)
    drop.grid(row=4, column=1)

    save_data = Button(top, text="Save")
    save_data.grid(row=5, column=1, pady=20)



#-------------Dimension------------------
dimension_label = Label(root, text="Dimension", fg="blue")
dimension_label.grid(row=0, column=0, padx=10, pady=10)

pool_depth_label = Label(root, text="Pool Depth:")
pool_depth_label.grid(row=1, column=0, padx=10, pady=10)
pool_depth_list = ["2 m", "3 m"]
clicked_depth = StringVar(root)
clicked_depth.set(pool_depth_list[0])
drop = OptionMenu(root, clicked_depth, *pool_depth_list)
drop.grid(row=1, column=1)

board_label = Label(root, text="No of Diving Boards:")
board_label.grid(row=2, column=0, padx=10, pady=10)
board_list = ["1 board"]
clicked_board = StringVar(root)
clicked_board.set(board_list[0])
drop = OptionMenu(root, clicked_board, *board_list)
drop.grid(row=2, column=1)


turn_over_time_label = Label(root, text="Turn Over Time:")
turn_over_time_label.grid(row=3, column=0, padx=10, pady=10)
turn_over_time_list = ["6 hours"]
clicked_turn_over_time = StringVar(root)
clicked_turn_over_time.set(turn_over_time_list[0])
drop = OptionMenu(root, clicked_turn_over_time, *turn_over_time_list)
drop.grid(row=3, column=1)

#-------------Inlet & Outlet------------------
inlet_outlet_label = Label(root, text="Inlet & Outlet", fg="green")
inlet_outlet_label.grid(row=0, column=2, padx=10, pady=10)

drainage_label = Label(root, text="No of Drain Pairs:")
drainage_label.grid(row=1, column=2, padx=10, pady=10)
drainage_list = ["1 pair", "2 pairs"]
clicked_drainage = StringVar(root)
clicked_drainage.set(drainage_list[0])
drop = OptionMenu(root, clicked_drainage, *drainage_list)
drop.grid(row=1, column=3)

#---------------Chlorine Requirement----------------------
chlorine_label = Label(root, text="Chlorine Requirement", fg="blue")
chlorine_label.grid(row=2, column=2, padx=10, pady=10)

chlorine_req_label = Label(root, text="Dose:")
chlorine_req_label.grid(row=3, column=2, padx=10, pady=10)
chlorine_req_list = ["1 mg/L", "2 mg/L", "3 mg/L", "10 mg/L"]
clicked_chlorine_req = StringVar(root)
clicked_chlorine_req.set(chlorine_req_list[0])
drop = OptionMenu(root, clicked_chlorine_req, *chlorine_req_list)
drop.grid(row=3, column=3)

chlorine_label_dose = Label(root, text="10 mg/L should be used only for supershocking pool", fg="red")
chlorine_label_dose.grid(row=4, column=3, padx=10, pady=10)

joints = Button(root, text="Add New Joints", command=add_joints)
joints.grid(row=5, column=2, padx=(20,20), pady=20)

#-------------Pump--------------------------------
inlet_outlet_label = Label(root, text="Pump", fg="red")
inlet_outlet_label.grid(row=0, column=4, padx=10, pady=10)


suction_head_label = Label(root, text="Suction Head 'S':")
suction_head_label.grid(row=1, column=4, padx=10, pady=10)
suction_head = Entry(root, width=30)
suction_head.grid(row=1, column=5, padx=10, pady=10)

discharge_head_label = Label(root, text="Discharge Head 'D':")
discharge_head_label.grid(row=2, column=4, padx=10, pady=10)
discharge_head = Entry(root, width=30)
discharge_head.grid(row=2, column=5, padx=10, pady=10)

#-------------Pipe-----------------
pipe_label = Label(root, text="Pipe", fg="blue")
pipe_label.grid(row=4, column=0, padx=10, pady=10)

drainage_suction_pipe_label = Label(root, text="Drain Suction Pipe Diameter:")
drainage_suction_pipe_label.grid(row=5, column=0, padx=10, pady=10)
drainage_suction_pipe_list = ["152.4 mm", "203.2 mm", "254 mm", "304.8 mm", "355.6 mm", "406.4 mm"]
clicked_drainage_suction_pipe = StringVar(root)
clicked_drainage_suction_pipe.set(drainage_suction_pipe_list[0])
drop = OptionMenu(root, clicked_drainage_suction_pipe, *drainage_suction_pipe_list)
drop.grid(row=5, column=1)

dsp_label = Label(root, text="Length of Drain Suction Pipe:")
dsp_label.grid(row=6, column=0, padx=10, pady=10)
dsp = Entry(root, width=30)
dsp.grid(row=6, column=1, padx=10, pady=10)

main_suction_pipe_label = Label(root, text="Main Suction Pipe Diameter:")
main_suction_pipe_label.grid(row=7, column=0, padx=10, pady=10)
main_suction_pipe_list = ["304.8 mm", "355.6 mm", "406.4 mm"]
clicked_main_suction_pipe = StringVar(root)
clicked_main_suction_pipe.set(main_suction_pipe_list[0])
drop = OptionMenu(root, clicked_main_suction_pipe, *main_suction_pipe_list)
drop.grid(row=7, column=1)

msp_label = Label(root, text="Length of Main Suction Pipe:")
msp_label.grid(row=8, column=0, padx=10, pady=10)
msp = Entry(root, width=30)
msp.grid(row=8, column=1, padx=10, pady=10)

main_return_inlet_pipe_label = Label(root, text="Main Return Inlet Pipe Diameter:")
main_return_inlet_pipe_label.grid(row=9, column=0, padx=10, pady=10)
main_return_inlet_pipe_list = ["304.8 mm", "355.6 mm", "406.4 mm"]
clicked_main_return_inlet_pipe = StringVar(root)
clicked_main_return_inlet_pipe.set(main_return_inlet_pipe_list[0])
drop = OptionMenu(root, clicked_main_return_inlet_pipe, *main_return_inlet_pipe_list)
drop.grid(row=9, column=1)

mrip_label = Label(root, text="Length of Main Return Inlet Pipe:")
mrip_label.grid(row=10, column=0, padx=10, pady=10)
mrip = Entry(root, width=30)
mrip.grid(row=10, column=1, padx=10, pady=10)


no_of_outlets_label = Label(root, text="Number of Return Inlets:")
no_of_outlets_label.grid(row=12, column=0, padx=10, pady=10)
no_of_outlets = Entry(root, width=30)
no_of_outlets.grid(row=12, column=1, padx=10, pady=10)


root.mainloop()