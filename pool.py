from tkinter import *
from datetime import *

root = Tk()
root.title(f"{datetime.now():%a, %b %d %Y} | Pool.io ")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("+%d+%d" % (300, 100))
root.config(background='white')

def pump_performance():
    pass

def pipe_size():
    pass


def design():
    top = Toplevel()
    top.title("Design for SI Unit")

    global pump_performance


    #-------------Dimension------------------
    dimension_label = Label(top, text="Dimension", fg="blue")
    dimension_label.grid(row=0, column=0, padx=10, pady=10)

    pool_depth_label = Label(top, text="Pool Depth:")
    pool_depth_label.grid(row=1, column=0, padx=10, pady=10)
    pool_depth_list = ["2m", "3m"]
    clicked_depth = StringVar(top)
    clicked_depth.set(pool_depth_list[0])
    drop = OptionMenu(top, clicked_depth, *pool_depth_list)
    drop.grid(row=1, column=1)

    board_label = Label(top, text="No of Diving Boards:")
    board_label.grid(row=2, column=0, padx=10, pady=10)
    board_list = ["1 board"]
    clicked_board = StringVar(top)
    clicked_board.set(board_list[0])
    drop = OptionMenu(top, clicked_board, *board_list)
    drop.grid(row=2, column=1)

    
    turn_over_time_label = Label(top, text="Turn Over Time:")
    turn_over_time_label.grid(row=3, column=0, padx=10, pady=10)
    turn_over_time_list = ["4 hours", "5 hours", "6 hours"]
    clicked_turn_over_time = StringVar(top)
    clicked_turn_over_time.set(turn_over_time_list[0])
    drop = OptionMenu(top, clicked_turn_over_time, *turn_over_time_list)
    drop.grid(row=3, column=1)



    #-------------Inlet & Outlet------------------
    inlet_outlet_label = Label(top, text="Inlet & Outlet", fg="green")
    inlet_outlet_label.grid(row=0, column=2, padx=10, pady=10)

    drainage_label = Label(top, text="No of Drain Pairs:")
    drainage_label.grid(row=1, column=2, padx=10, pady=10)
    drainage_list = ["1 pair", "2 pairs", "3 pairs", "4 pairs"]
    clicked_drainage = StringVar(top)
    clicked_drainage.set(drainage_list[0])
    drop = OptionMenu(top, clicked_drainage, *drainage_list)
    drop.grid(row=1, column=3)

    no_of_outlets_label = Label(top, text="Number of Return Inlets:")
    no_of_outlets_label.grid(row=2, column=2, padx=10, pady=10)
    no_of_outlets = Entry(top, width=30)
    no_of_outlets.grid(row=2, column=3, padx=10, pady=10)

    flow_rate_label = Label(top, text="Flow Rate for single overhead pipe:")
    flow_rate_label.grid(row=3, column=2, padx=10, pady=10)
    flow_rate_list = [""]
    clicked_flow_rate = StringVar(top)
    clicked_flow_rate.set(flow_rate_list[0])
    drop = OptionMenu(top, clicked_flow_rate, *flow_rate_list)
    drop.grid(row=3, column=3)


    #-------------Pump--------------------------------
    inlet_outlet_label = Label(top, text="Pump", fg="red")
    inlet_outlet_label.grid(row=0, column=4, padx=10, pady=10)


    suction_head_label = Label(top, text="Suction Head 'S':")
    suction_head_label.grid(row=1, column=4, padx=10, pady=10)
    suction_head = Entry(top, width=30)
    suction_head.grid(row=1, column=5, padx=10, pady=10)

    discharge_head_label = Label(top, text="Discharge Head 'D':")
    discharge_head_label.grid(row=2, column=4, padx=10, pady=10)
    discharge_head = Entry(top, width=30)
    discharge_head.grid(row=2, column=5, padx=10, pady=10)

    friction_head_label = Label(top, text="Friction Head 'F:")
    friction_head_label.grid(row=3, column=4, padx=10, pady=10)
    friction_head = Entry(top, width=30)
    friction_head.grid(row=3, column=5, padx=10, pady=10)

    #-------------Pipe-----------------
    pipe_label = Label(top, text="Pipe", fg="blue")
    pipe_label.grid(row=4, column=0, padx=10, pady=10)

    drainage_suction_pipe_label = Label(top, text="Drain Suction Pipe:")
    drainage_suction_pipe_label.grid(row=5, column=0, padx=10, pady=10)
    drainage_suction_pipe_list = ["152.4 mm", "203.2 mm", "254 mm", "304.8 mm", "355.6 mm", "406.4 mm"]
    clicked_drainage_suction_pipe = StringVar(top)
    clicked_drainage_suction_pipe.set(drainage_suction_pipe_list[0])
    drop = OptionMenu(top, clicked_drainage_suction_pipe, *drainage_suction_pipe_list)
    drop.grid(row=5, column=1)

    dsp_label = Label(top, text="Length")
    dsp_label.grid(row=6, column=0, padx=10, pady=10)
    dsp = Entry(top, width=30)
    dsp.grid(row=6, column=1, padx=10, pady=10)

    main_suction_pipe_label = Label(top, text="Main Suction Pipe:")
    main_suction_pipe_label.grid(row=7, column=0, padx=10, pady=10)
    main_suction_pipe_list = ["304.8 mm", "355.6 mm", "406.4 mm"]
    clicked_main_suction_pipe = StringVar(top)
    clicked_main_suction_pipe.set(main_suction_pipe_list[0])
    drop = OptionMenu(top, clicked_main_suction_pipe, *main_suction_pipe_list)
    drop.grid(row=7, column=1)

    msp_label = Label(top, text="Length")
    msp_label.grid(row=8, column=0, padx=10, pady=10)
    msp = Entry(top, width=30)
    msp.grid(row=8, column=1, padx=10, pady=10)

    main_return_inlet_pipe_label = Label(top, text="Main Return Inlet Pipe:")
    main_return_inlet_pipe_label.grid(row=9, column=0, padx=10, pady=10)
    main_return_inlet_pipe_list = ["304.8 mm", "355.6 mm", "406.4 mm"]
    clicked_main_return_inlet_pipe = StringVar(top)
    clicked_main_return_inlet_pipe.set(main_return_inlet_pipe_list[0])
    drop = OptionMenu(top, clicked_main_return_inlet_pipe, *main_return_inlet_pipe_list)
    drop.grid(row=9, column=1)

    mrip_label = Label(top, text="Length")
    mrip_label.grid(row=10, column=0, padx=10, pady=10)
    mrip = Entry(top, width=30)
    mrip.grid(row=10, column=1, padx=10, pady=10)

    chlorine_req_label = Label(top, text="Main Return Inlet Pipe:")
    chlorine_req_label.grid(row=11, column=0, padx=10, pady=10)
    chlorine_req_list = ["1 mg/L", "2 mg/L", "3 mg/L", "10 mg/L"]
    clicked_chlorine_req = StringVar(top)
    clicked_chlorine_req.set(chlorine_req_list[0])
    drop = OptionMenu(top, clicked_chlorine_req, *chlorine_req_list)
    drop.grid(row=11, column=1)

    chlorine_label = Label(top, text="10 mg/L should be used only for supershocking pool", fg="red")
    chlorine_label.grid(row=12, column=1, padx=10, pady=10)




design = Button(root, text="Design", bg="green", command=design)
design.grid(row=1, column=0,  padx=(20,20), pady=20)

#unit_list = ["SI Unit", "Metric Unit"]
#clicked_unit = StringVar(root)
#clicked_unit.set(unit_list[0])
#drop = OptionMenu(root, clicked_unit, *unit_list)
#drop.grid(row=0, column=0)

pipe_size = Button(root, text="Pipe Size Chart", bg="blue", command=pipe_size)
pipe_size.grid(row=1, column=1, padx=(20,20), pady=20)

pump_performance = Button(root, text="Pump Performance Curve", bg="grey", command=pump_performance)
pump_performance.grid(row=1, column=2, padx=(20,20), pady=20)





root.mainloop()