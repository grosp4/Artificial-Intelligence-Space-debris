import gtk
import matplotlib.pyplot as plt
import Patrick
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas

#  ******************************************************************************/
#  *  local variables
#  ******************************************************************************/
pathname = '\dataset'   # pathname to get to a specific folder
debug = 1               # debug value 0 = no debug
printInNewPlot = 0      # 0 = no new plot, using old one
plotmode = 0            # 0 = 2D mode, 1 = 3D Mode
dataset = "None"
# /******************************************************************************/
# /** \file          Class baseWindow
#  *  \brief         TBD
#  *******************************************************************************
#  *
#  *
#  *
#  *  \brief         TBD
#  *
#  *  \authors       grosp4,
#  *
#  *  \date          22.11.2015
#  *
#  *  \remark        Last Modification
#  *                  \li grosp4,  22.11.2015, Created
#  *
#  *
#  ******************************************************************************/
# /*
#  *  functions:     __init__
#  *                main
#  *                destroyOurWindow
#  *
#  ******************************************************************************/
class baseWindow:

#******************************************************************************/
# /*
#  *     functionname:          @ __init__
#  *     parameter:             @
#  *     returns:               @
#  *     description:           @
#  *
#  *
#*******************************************************************************/
    def __init__(self):

            # setting windows properties starts here
            self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
            self.window.set_title("Space debris GUI")
            self.window.set_default_size(1280,720)
            self.window.connect("destroy",self.destroyOurWindow)

            # Buttons creation starts here
            self.Button_Training = gtk.Button("Train me")
            self.Button_Training.connect("clicked", self.testfunc)

            self.Button_PlotData = gtk.Button("Plot Data ")
            self.Button_PlotData.connect("clicked", self.testfunc)

            self.Button_Exit = gtk.Button("Exit")
            self.Button_Exit.connect("clicked", self.destroyOurWindow)

            # Checkbutton creating starts here
            self.NewPlotButton = gtk.CheckButton("New Plot Window")
            self.NewPlotButton.connect("toggled",self.changeOfNewPlot)

            # label creating starts here
            # distance labels are between buttons, and enumerated from top to down (1 is uppest one)
            self.label_distance_1 = gtk.Label(" ")
            self.label_distance_2 = gtk.Label(" ")
            self.label_distance_3 = gtk.Label(" ")
            self.label_distance_4 = gtk.Label(" ")
            self.label_distance_5 = gtk.Label(" ")
            self.label_distance_6 = gtk.Label(" ")
            self.label_status = gtk.Label("ready")
            self.label_warning= gtk.Label("Warning! All old plots will be deleted! ")

            #switch buttom creating starts here
            self.combo_between_2D_and_3D_Plot = gtk.combo_box_new_text()
            self.combo_between_2D_and_3D_Plot.set_entry_text_column(0)
            self.combo_between_2D_and_3D_Plot.connect("changed", self.getPlotmode)
            self.combo_dataset = gtk.combo_box_new_text()
            self.combo_dataset.connect("changed", self.getDatasetToPlot)




            # populate the comboboxes
            self.combo_between_2D_and_3D_Plot.append_text("2D Plot")
            self.combo_between_2D_and_3D_Plot.append_text("3D Plot")
            self.combo_between_2D_and_3D_Plot.set_active(0)

            #get data files in write them into a combobox
            List_data_for_combo_box = Patrick.getAllDatasetFileNames(pathname)
            if debug:
                    print List_data_for_combo_box

            # write all files into the combobox
            currentListElement = 0
            while currentListElement <len(List_data_for_combo_box):
                     if debug:
                             print List_data_for_combo_box[currentListElement]
                     # add to combobox
                     self.combo_dataset.append_text(List_data_for_combo_box[currentListElement])
                     currentListElement+=1
            #set combobox active
            self.combo_dataset.set_active(0)

            # container creating starts here
            self.box_container_horizontal = gtk.HBox()
            self.box_container_vertical_left = gtk.VBox()
            self.box_container_vertical_left.set_border_width(7)
            self.box_container_vertical_right = gtk.VBox()

            # containter alignment starts here
            self.box_container_vertical_left.set_size_request(250, 500)
            self.box_container_horizontal.pack_start(self.box_container_vertical_left,expand=False, fill=False, padding=False)
            self.box_container_horizontal.pack_start(self.box_container_vertical_right,expand=True, fill=True, padding=False)

            self.box_container_vertical_left.pack_start(self.Button_Training, expand=False, fill=False)
            self.Button_Training.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.label_distance_1,expand=False, fill=False, padding=False)
            self.label_distance_1.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.NewPlotButton,expand=True, fill=False, padding=False)
            self.NewPlotButton.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.label_warning,expand=False, fill=False, padding=False)
            self.label_warning.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.label_distance_2,expand=False, fill=False, padding=False)
            self.label_distance_2.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.combo_between_2D_and_3D_Plot,expand=False, fill=False, padding=False)
            self.combo_between_2D_and_3D_Plot.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.label_distance_3,expand=False, fill=False, padding=False)
            self.label_distance_3.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.combo_dataset,expand=True, fill=False, padding=False)
            self.combo_dataset.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.label_distance_4,expand=True, fill=False, padding=False)
            self.label_distance_4.set_size_request(200, 10)

            self.box_container_vertical_left.pack_start(self.Button_PlotData, expand=False, fill=False)
            self.Button_PlotData.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.label_distance_5,expand=False, fill=False, padding=False)
            self.label_distance_5.set_size_request(200, 300)

            self.box_container_vertical_left.pack_start(self.Button_Exit, expand = False, fill = False)
            self.Button_Exit.set_size_request(200, 40)

            self.box_container_vertical_left.pack_start(self.label_distance_6,expand=True, fill=False, padding=False)
            self.label_distance_6.set_size_request(200, 20)

            self.box_container_vertical_left.pack_start(self.label_status,expand=True, fill=False, padding=False)
            self.label_status.set_size_request(200, 20)

            # aligning properties of widgets
            self.label_status.set_alignment(0.1,0.1)

            if debug:
                f = plt.figure()
                a = f.add_subplot(111)
                t = [1,2,3,4]
                s = [1,2,3,5]
                a.plot(t, s)
                self.canvas = FigureCanvas(f)
                self.box_container_vertical_right.pack_start(self.canvas, True, True, 0)

            ## add elements to our window
            self.window.add(self.box_container_horizontal)

            # has to be the last function that is called in init, because afterwards is no refresh
            self.window.show_all()
            #hide warning layer as it is only shown if you press "new plot"
            self.label_warning.hide()


#  ******************************************************************************/
# /*
#  *     functionname:          @ testfunc
#  *     parameter:             @
#  *     returns:               @
#  *     description:           @
#  *
#  *
#  *******************************************************************************/
    def plot(self,widget):
            if debug:
                print "entering plotmode"
            self.label_status.set_text(widget.get_label())


#  ******************************************************************************/
# /*
#  *     functionname:          @ main(self)
#  *     parameter:             @
#  *     returns:               @
#  *     description:           @
#  *
#  *
#  *******************************************************************************/
    def main(self):
            gtk.main()


#  ******************************************************************************/
# /*
#  *     functionname:          @ destroyOurWindow
#  *     parameter:             @
#  *     returns:               @
#  *     description:           @
#  *
#  *
#  *******************************************************************************/
    def destroyOurWindow ( self, widget, data = None):
            gtk.main_quit()


#  ******************************************************************************/
# /*
#  *     functionname:          @ changeOfNewPlot
#  *     parameter:             @
#  *     returns:               @
#  *     description:           @
#  *
#  *
#  *******************************************************************************/
    def changeOfNewPlot(self, widget, data = None):
            global printInNewPlot

            if printInNewPlot:
                printInNewPlot = False
                self.label_warning.hide()
                self.label_distance_2.show()

            else:
                printInNewPlot = True
                self.label_warning.show()
                self.label_distance_2.hide()

            if debug:
                print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])
                print printInNewPlot


#  ******************************************************************************/
# /*
#  *     functionname:          @ getPlotmode
#  *     parameter:             @
#  *     returns:               @
#  *     description:           @
#  *
#  *
#  *******************************************************************************/
    def getPlotmode(self, widget):
            global plotmode
            text = widget.get_active_text()
            self.label_status.set_text(" %s plotmode choosen" % text)
            if text =="2D Plot":
                plotmode = 0
            else:
                plotmode = 1

            if debug:
                print("Selected: %s " % text)


#  ******************************************************************************/
# /*
#  *     functionname:          @ getPlotmode
#  *     parameter:             @
#  *     returns:               @
#  *     description:           @
#  *
#  *
#  *******************************************************************************/
    def getDatasetToPlot(self,widget):
            global dataset
            dataset = widget.get_active_text()
            self.label_status.set_text("%s choosen" % dataset)
            if debug:
                print("Selected: %s " % dataset)


#  debug main
if __name__ == "__main__":

    base = baseWindow()
    base.main()