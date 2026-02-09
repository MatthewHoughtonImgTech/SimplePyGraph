from queue import Queue
from threading import Thread
import dearpygui.dearpygui as dpg


def runGraphWindow(pipeIn : Queue):
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()
    dpg.set_global_font_scale(3)
    pExample = {
        "name" : {"xvals" : [], "yvals" : []}
    }
    plots = {}
    with dpg.window(label="Loss Graph", width=-1, height=-1):
        with dpg.plot(label="lossgraph",width=-1, height=-1):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="itteration")
            dpg.add_plot_axis(dpg.mvYAxis, label="loss", tag='y_axis')

            #for name in plots.keys():
                #dpg.add_line_series( plots[name]["xvals"], plots[name]["yvals"],label=name, tag=plots[name], parent="y_axis")
        dpg.add_text("Hello world!")

    dpg.show_viewport()
    #dpg.start_dearpygui()
    while dpg.is_dearpygui_running():
        if not pipeIn.empty():
            entry = pipeIn.get()
            name = entry["name"]
            if name not in plots:
                plots[name] = {"xvals" : [], "yvals" : []}
                dpg.add_line_series( [1.], [2.],label=name, tag=name, parent='y_axis')
            plots[name]["xvals"].append(float(entry["xval"]))
            plots[name]["yvals"].append(float(entry["yval"]))
            dpg.configure_item(name, x=plots[name]["xvals"], y=plots[name]["yvals"])
        dpg.render_dearpygui_frame()
            
    dpg.destroy_context()

def createGraphWindow():
    q = Queue()
    p = Thread(target=runGraphWindow, args=(q,))
    p.start()
    return q