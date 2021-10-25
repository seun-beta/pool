from tkinter import *
from tkinter import messagebox
from datetime import *
import sqlite3
import math 


#------------------Constants----------------------



conn = sqlite3.connect("pool.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS "Joints" (
"joints_id"	INTEGER NOT NULL UNIQUE PRIMARY KEY,
"type_of_joint"	TEXT,
"type_of_joint_diameter" REAL);
""")

root = Tk()
root.title(f"{datetime.now():%a, %b %d %Y} | Pool.io ")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("+%d+%d" % (300, 100))



def calculate():

    bathing_load = int(((30*25)/1.8580) + ((20*25)/1.8580) - 27.87)
    print(str(bathing_load)+ "\n")


    if clicked_depth.get() == "2 m":
        turn_over_rate = str(4161.23/6) + " m3/hr"
    else:
        turn_over_rate = str(5411.23/6) + " m3/hr"
    print(turn_over_rate+ "\n")

    
    if int(no_of_inlets.get()) < 73 and clicked_depth.get() == "2 m":
            messagebox.showerror("Error!", "No of inlets must be greater than 73 for 2m pool")
    elif int(no_of_inlets.get()) < 95 and clicked_depth.get() == "3 m":
        messagebox.showerror("Error!", "No of inlets must be greater than 95 for 3m pool")
    else:
        turn_over_rate = turn_over_rate.split()
        return_inlet_flow_rate = float(turn_over_rate[0]) / float(no_of_inlets.get())
        return_inlet_flow_rate = str(return_inlet_flow_rate) + " m3/hr"
        print(return_inlet_flow_rate+ "\n")


    Q= float(turn_over_rate.split[0])
    dsp_value = clicked_drainage_suction_pipe.get().split()
    new_dsp_value = dsp_value[0]
    dsp_s = ((Q*0.2)/(1000.8*150)*(float(new_dsp_value)/1000)**2.63)**(1/0.54)
    print(dsp_s)
    dsp_hl = dsp_s * float(dsp.get())
    print(dsp_hl)
    print("")

    msp_value = clicked_main_suction_pipe.get().split()
    new_msp_value = msp_value[0]
    msp_s = ((Q)/(1000.8*150)*(float(new_msp_value)/1000)**2.63)**(1/0.54)
    print(msp_s)
    msp_hl = msp_s * float(msp.get())
    print(msp_hl)
    print("")

    mrip_value = clicked_main_return_inlet_pipe.get().split()
    new_mrip_value = mrip_value[0]
    mrip_s = ((Q)/(1000.8*150)*(float(new_mrip_value)/1000)**2.63) **(1/0.54)
    print(mrip_s)
    mrip_hl = mrip_s * float(mrip.get())
    print(mrip_hl)



    #if clicked_drainage.get() == "1 pair":
    #    turn_over_rate = turn_over_rate.split()
    #    print(turn_over_rate)
    #    Q = 0.2 * float(turn_over_rate[0])
    #    V = 0.914
    #    drainage_size = math.sqrt((4*Q)/(3.142*V))
    #elif clicked_drainage.get() == "2 pairs":
    #    turn_over_rate = turn_over_rate.split()
    #    print(turn_over_rate)
    #    Q = 0.1 * float(turn_over_rate[0])
    #    V = 0.914
    #    drainage_size = math.sqrt((4*Q)/(3.142*V))
    #print(str(drainage_size)+ "\n")


def add_joints():

    def save_joints():
        conn = sqlite3.connect("pool.db")
        cur = conn.cursor()

        toj = clicked_toj.get()
        toj_diameter = clicked_toj_diameter.get().split()


        cur.execute("INSERT INTO Joints VALUES (null,?,?)",(
                    toj,
                    toj_diameter[0])
        )
        conn.commit()
        conn.close()
        success = Label(top, text="Added record successfully", fg="green")
        success.grid(row=4, column=1, columnspan=2)
        success.after(2000, success.destroy)



    def delete_joints():
        conn = sqlite3.connect("pool.db")
        cur = conn.cursor()

        cur.execute("DELETE FROM Joints;")
        conn.commit()
        conn.close()
        success = Label(top, text="Deleted all records successfully", fg="red")
        success.grid(row=6, column=1, columnspan=2)
        success.after(5000, success.destroy)

    #-------------Joints------------------
    top = Toplevel()
    top.geometry("+%d+%d" % (300, 100))

    toj_label = Label(top, text="Type of Joint:")
    toj_label.grid(row=1, column=0, padx=10, pady=10)
    toj_list = ["Tee Joint", "90° Elbow", "Long Elbow", "45° Elbow"]
    clicked_toj = StringVar(top)
    clicked_toj.set(toj_list[0])
    drop = OptionMenu(top, clicked_toj, *toj_list)
    drop.grid(row=1, column=1)

    toj_diameter_label = Label(top, text="Joint Diameter: ")
    toj_diameter_label.grid(row=2, column=0, padx=10, pady=10)

    toj_diameter_list = ["152.4 mm", "203.2 mm", "254 mm", "304.8 mm", "355.6 mm", "406.4 mm"] 
    clicked_toj_diameter = StringVar(top)
    clicked_toj_diameter.set(toj_diameter_list[0])
    drop = OptionMenu(top, clicked_toj_diameter, *toj_diameter_list)
    drop.grid(row=2, column=1)


    save_data = Button(top, text="Save", command=save_joints)
    save_data.grid(row=3, column=1, pady=20)

    clear_data = Button(top, text="Clear ALL Data", bg="red",  command=delete_joints)
    clear_data.grid(row=5, column=1, pady=20)



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

calculate = Button(root, text="Calculate", command=calculate)
calculate.grid(row=7, column=2, padx=(40,40), pady=20)

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


no_of_inlets_label = Label(root, text="Number of Return Inlets:")
no_of_inlets_label.grid(row=12, column=0, padx=10, pady=10)
no_of_inlets = Entry(root, width=30)
no_of_inlets.grid(row=12, column=1, padx=10, pady=10)




root.mainloop()