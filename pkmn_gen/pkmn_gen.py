from tkinter import *
from pkmn_class import *
from pkmn_plt import *
from random import *

window = Tk()
window.title("PKMN GENERATOR v1.0")
window.config(bg="#fcfcfc")
window.geometry("517x418")
window.resizable(width=False,height=False)

#the result for export
export_set = StringVar()

def Generate():
    #get stat and make monster class
    stat_total = ( randint(min_stat.get(),max_stat.get()) // 10) * 10
    gen_pkmn = Monster(opt1_text.get(),opt2_text.get(),type.get(),ability.get(),stat.get(),stat_total)

    #export
    export_setting = ""
    #get halves and output
    name = gen_pkmn.print_name()
    monsters = gen_pkmn.print_monster()

    monster_text.set(monsters[0].capitalize()+" "+monsters[1].capitalize())
    name_text.set(name.capitalize())

    #add name to export
    export_setting += name.capitalize() + "\n"

    #check if they need type
    if type.get():
        types = gen_pkmn.print_type()
        cols = gen_pkmn.print_type_col()
        type_text.set(types[0])
        type_col1.set(cols[0])
        if types[1] == "None":
            type_text_2.set("")
            type_col2 .set("#fcfcfc")
        else:
            type_text_2.set(types[1])
            type_col2.set(cols[1])

        # add type
        export_setting += types[0] + " " + types[1] + "\n"

    else:
        type_text.set("")
        type_text_2.set("")
        type_col1.set("#fcfcfc")
        type_col2.set("#fcfcfc")


    #Check if they need ability
    if ability.get():
        ability_text.set(gen_pkmn.print_ability())
        # add ability
        export_setting += gen_pkmn.print_ability() + "\n"
    else:
        ability_text.set("")


    for widget in stat_table.winfo_children():
        widget.destroy()
    #check if stat
    if stat.get():
        Label(stat_table, text="HP:", bg="#fcfcfc").grid(row=0, column=0)
        Label(stat_table, text="Attack:", bg="#fcfcfc").grid(row=1, column=0)
        Label(stat_table, text="Sp. Attack:", bg="#fcfcfc").grid(row=2, column=0)
        Label(stat_table, text="Defense:", bg="#fcfcfc").grid(row=3, column=0)
        Label(stat_table, text="Sp. Defense:", bg="#fcfcfc").grid(row=4, column=0)
        Label(stat_table, text="Speed:", bg="#fcfcfc").grid(row=5, column=0)
        Label(stat_table, text="Stat Total:", bg="#fcfcfc").grid(row=6, column=0)

        stats = gen_pkmn.print_stat()
        hp.set(stats["HP"])
        atk.set(stats["ATK"])
        spatk.set(stats["SPATK"])
        df.set(stats["DEF"])
        spdf.set(stats["SPDEF"])
        spd.set(stats["SPD"])
        st.set(stat_total)

        Label(stat_table, textvariable=hp, bg="#fcfcfc").grid(row=0, column=1)
        Label(stat_table, textvariable=atk, bg="#fcfcfc").grid(row=1, column=1)
        Label(stat_table, textvariable=spatk, bg="#fcfcfc").grid(row=2, column=1)
        Label(stat_table, textvariable=df, bg="#fcfcfc").grid(row=3, column=1)
        Label(stat_table, textvariable=spdf, bg="#fcfcfc").grid(row=4, column=1)
        Label(stat_table, textvariable=spd, bg="#fcfcfc").grid(row=5, column=1)
        Label(stat_table, textvariable=st, bg="#fcfcfc").grid(row=6, column=1)


    #palette
    for widget in plt_table.winfo_children():
        widget.destroy()
    if colour.get():
        pal = palette(colour_mode.get())
        rgb_list = pal.get_plt()
        hex_list = pal.rgb_hex(rgb_list)
        x = 0
        for col in hex_list:
            Label(plt_table,text=str(col),fg="#ffffff",bg=col,width=8,height=4,anchor=S,font=("Helvetica",12,'bold')).grid(row=0,column=0+x)
            #add colour
            export_setting += col + "\n"
            x+=1
        plt_table.grid(row=7)

    for widget in basic_table.winfo_children():
        widget.destroy()
    Label(basic_table, textvariable=monster_text, bg="#fcfcfc").grid(row=1, column=0, columnspan=2)
    Label(basic_table, textvariable=type_text, bg=type_col1.get(),fg="#fcfcfc",width=10).grid(row=2, column=0)
    Label(basic_table, textvariable=type_text_2, bg=type_col2.get(),fg="#fcfcfc",width=10).grid(row=2, column=1)
    Label(basic_table, textvariable=ability_text, bg="#fcfcfc").grid(row=3, column=0, columnspan=2)
    Label(basic_table, textvariable=name_text, font=(24), bg="#fcfcfc").grid(row=0, column=0, columnspan=2)

    export_set.set(export_setting)

def Export(settings):
    export = Toplevel(window)
    export.title("EXPORT")
    export.geometry("200x200")
    ans = settings.get()
    Label(export,text="Settings exported...").grid(row=0,columnspan=2)
    text = Text(export,height=20,width=25)
    text.grid(row=1,columnspan=2)
    text.insert(END,ans)


#window.geometry("500x500")
Label(window,text="Too lazy to think of a Pokemon design? Then random generate one!",font=("Helvetica",10),bg="#fcfcfc").grid(row=0,column=0,columnspan=2)

#Option 1 dropdown
opt1_text = StringVar()
opt1_text.set("animal")
opt1 = OptionMenu(window,opt1_text,"animal","object")
opt1.config(bg="#fcfcfc",highlightthickness=0,indicatoron=0,width=20,anchor=SW)
opt1["menu"].config(bg="#fcfcfc",activebackground="#ebebeb",activeforeground="black")
opt1.grid(row=1,column=0)

#Option 2 dropdown
opt2_text = StringVar(window)
opt2_text.set("animal")
opt2 = OptionMenu(window,opt2_text,"animal","object")
opt2.config(bg="#fcfcfc",highlightthickness=0,indicatoron=0,width=20,anchor=SW)
opt2["menu"].config(bg="#fcfcfc",activebackground="#ebebeb",activeforeground="black")
opt2.grid(row=1,column=1)

#Frames
check_boxes = Frame(window,bg="#fcfcfc")
check_boxes.grid(row=4,columnspan=2)

basic_table = Frame(window,bg="#fcfcfc")
basic_table.grid(row=6,column=0)

#CheckButtons
type = BooleanVar()
ran_type = Checkbutton(check_boxes, text="Random Type", variable=type,onvalue=True, offvalue=False, font=("Helvetica",8),bg="#fcfcfc")
ran_type.grid(row=0,column=0)

ability = BooleanVar()
ran_ability = Checkbutton(check_boxes, text="Random Ability", variable=ability,onvalue=True, offvalue=False, font=("Helvetica",8),bg="#fcfcfc")
ran_ability.grid(row=1,column=1)

stat = BooleanVar()
ran_stats = Checkbutton(check_boxes, text="Random Stats", variable=stat,onvalue=True, offvalue=False, font=("Helvetica",8),bg="#fcfcfc")
ran_stats.grid(row=1,column=0)

min_stat = IntVar()
min_stat.set(200)
min_ent = Entry(check_boxes,textvariable=min_stat,bg="#fcfcfc")
min_ent.grid(row=2,column=1)
Label(check_boxes,text="Minimum Stat Total:",anchor=E,font=("Helvetica",8),bg="#fcfcfc").grid(row=2,column=0)

max_stat = IntVar()
max_stat.set(300)
max_ent = Entry(check_boxes,textvariable=max_stat,bg="#fcfcfc")
max_ent.grid(row=3,column=1)
Label(check_boxes,text="Maximum Stat Total:", anchor=E,font=("Helvetica",8),bg="#fcfcfc").grid(row=3,column=0)

colour = BooleanVar()
ran_colour = Checkbutton(check_boxes, text="Random Colour Palette", variable=colour,onvalue=True, offvalue=False, font=("Helvetica",8),bg="#fcfcfc")
ran_colour.grid(row=4,column=0)
colour_mode = StringVar()
colour_mode.set("Complementary")
colour_mode_menu = OptionMenu(check_boxes,colour_mode,"Complementary","Analogous","Triadic","Split Complementary")
colour_mode_menu.config(bg="#fcfcfc",highlightthickness=0,indicatoron=0,width=20)
colour_mode_menu["menu"].config(bg="#fcfcfc",activebackground="#ebebeb",activeforeground="black")
colour_mode_menu.grid(row=4,column=1)

monster_text = StringVar()
monster_text.set("")
type_text = StringVar()
type_text_2 = StringVar()
type_text.set("")
type_text_2.set("")
ability_text = StringVar()
ability_text.set("")
name_text = StringVar()
name_text.set("")
type_col1 = StringVar()
type_col1.set("#fcfcfc")
type_col2 = StringVar()
type_col2.set("#fcfcfc")

#Stats
stat_table = Frame(window,bg="#fcfcfc")
stat_table.grid(row=6,column=1)

hp = StringVar()
atk = StringVar()
spatk = StringVar()
df = StringVar()
spdf = StringVar()
spd = StringVar()
st = StringVar()

hp.set("")
atk.set("")
spatk.set("")
df.set("")
spdf.set("")
spd.set("")
st.set("")

#stats
hp_l = Label(stat_table,textvariable=hp,bg="#fcfcfc").grid(row=0,column=1)
atk_l = Label(stat_table,textvariable=atk,bg="#fcfcfc").grid(row=1,column=1)
spatk_l = Label(stat_table,textvariable=spatk,bg="#fcfcfc").grid(row=2,column=1)
df_l = Label(stat_table,textvariable=df,bg="#fcfcfc").grid(row=3,column=1)
spdf_l = Label(stat_table,textvariable=spdf,bg="#fcfcfc").grid(row=4,column=1)
spd_l = Label(stat_table,textvariable=spd,bg="#fcfcfc").grid(row=5,column=1)
st_l = Label(stat_table,textvariable=st,bg="#fcfcfc").grid(row=6,column=1)

#Generate buttton
done_but = Button(window,text="Generate!",command=lambda:Generate(),bg="#fcfcfc",width=20,border=1)
done_but.grid(row=5,column=1)

#Export button
export_but = Button(window,text="Export Settings",command=lambda:Export(export_set),bg="#fcfcfc",width=20,border=1)
export_but.grid(row=5,column=0)

#colour
plt_table = Frame(window)
plt_table.config(borderwidth=1,relief=SUNKEN,bg="#fcfcfc")
plt_table.grid(row=7,columnspan=2)
for i in range(6):
    Label(plt_table,text="",bg="#fcfcfc",width=8,height=4,anchor=S,font=("Helvetica",12,'bold')).grid(row=0,column=i)


window.mainloop()
