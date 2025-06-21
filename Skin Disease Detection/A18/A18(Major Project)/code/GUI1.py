import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import webbrowser
import keras
import numpy as np
#import plotfile
import tensorflow
class CropDiseasePrediction(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Crop Disease Prediction')
        self.geometry('900x600')
        self.configure(bg="#fff")
        self.resizable(False, False)
        
        self.main_img_path = 'C:/Users/91701/Desktop/New folder/bgimage/bg.png'  # Placeholder for main window background image path
        self.result_img_path =  'C:/Users/91701/Desktop/New folder/bgimage/bg.png'  # Placeholder for result frame image path
        #self.plot_image_path = 'C:/Users/91701/propyt/project/plt.png'
        #self.down = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0e\x00\x00\x00\x07\x08\x06\x00\x00\x008G|\x19\x00\x00\x00\tpHYs\x00\x00\x10\x9b\x00\x00\x10\x9b\x01t\x89\x9cK\x00\x00\x00\x19tEXtSoftware\x00www.inkscape.org\x9b\xee<\x1a\x00\x00\x00OIDAT\x18\x95\x95\xce\xb1\x0e@P\x0cF\xe1\xefzI\x8fc$\x12\x111\x19\xec\x9e\x12\xcb\x95 A\x9d\xa4K\xff\x9e\xb6\t\x13J\xffX \xa1\xc7\x16\xac\x19\xc5\xb1!*\x8fy\xf6BB\xf7"\r_\xff77a\xcd\xbd\x10\xedI\xaa\xa3\xd2\xf9r\xf5\x14\xee^N&\x14\xab\xef\xa9\'\x00\x00\x00\x00IEND\xaeB`\x82'
        
        self.img = None
        #self.thrd = None
        self.result_frame = None  # Initialize the result_frame attribute
        self.loading_frame = None  # Initialize the loading_frame attribute
        self.loading_progressbar = None  # Placeholder for the progress bar
        self.url = ""
        self.setup_gui()

    def setup_gui(self):
        self.setup_main_window()
        
    def setup_main_window(self):
        # Load and display the main window background image
        self.main_img = tk.PhotoImage(file=self.main_img_path)
        self.label = tk.Label(self, image=self.main_img)
        self.label.place(x=0, y=0)

        # Heading
        self.heading = tk.Label(self, text="CROP DISEASE PREDICTION", fg="DarkGreen", bg="#EAA667", font=("Times", 32, 'bold'))
        self.heading.place(x=450, y=60, anchor="center")

        # Input box
        #self.Tname = tk.Entry(self, width=40, fg='gray', border=0, bg='white', font=('Times', 17), justify='center')
        #self.Tname.place(relx=0.5, y=214, anchor="center")
        #self.Tname.insert(0, 'Enter Ticker Symbol')
        #self.Tname.bind('<FocusIn>', self.on_entry_click)
        #self.Tname.bind('<FocusOut>', self.on_focus_out)
        
        tk.Button(self, text='Upload Leaf Image',width=30,bg='white', fg='Green', border=0,command = self.upload_file,font=('Times', 17), justify='center').place(relx=0.5, y=165, anchor="center") 

        # Underline
        #tk.Frame(self, width=450, height=2, bg="black").place(relx=0.5, y=227, anchor="center")

        # Forecast button
        tk.Button(self, width='35', pady='7', text='Predict', bg='Green', fg='white', border=0,
                  command=self.submit).place(relx=0.5, y=485, anchor="center")
    def callback(self):
        print(self.url)
        webbrowser.open_new(self.url)

    def setup_result_frame(self):
        # Load and display an image in the result frame
        result_img = tk.PhotoImage(file=self.main_img_path)
        self.resultbg = tk.Label(self.result_frame, image=result_img)
        self.resultbg.image = result_img
        self.resultbg.place(x=0, y=0)
        
        self.plot = tk.Frame(self, width=260, height=260)
        self.plot.place(relx = 0.5,y = 200, anchor="center")
        predictions=['Blueberry___healthy','Squash___Powdery_mildew','Grape___Leaf_blight',
        'Apple___apple_Cedar_rust','Tomato___healthy','Tomato___Bacterial_spot','Tomato___Septoria_leaf_spot', 'Corn_(maize)___healthy','Tomato___Late_blight','Potato___Early_blight','Grape___Black_Measles',
        'Corn_(maize)___Common_rust_','Soybean___healthy','Apple___healthy','Cherry___Powdery_mildew','Potato___healthy','Tomato___Early_blight',
        'Apple___Black_rot','Tomato___Target_Spot','Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Strawberry___Leaf_scorch','Potato___Late_blight',
        'Peach___Bacterial_spot','Strawberry___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Tomato___Leaf_Mold','Raspberry___healthy', 'Tomato___mosaic_virus',
        'Grape___Black_rot','Pepper,_bell___Bacterial_spot', 'Grape___healthy','Tomato___Tomato_Yellow_Leaf_Curl_Virus',
        'Peach___healthy','Tomato___Spider_mites Two-spotted_spider_mite', 'Pepper_bell___healthy','Cherry___healthy','Apple___Apple_scab']
        #plot_image = tk.PhotoImage(file=self.plot_image_path)
        #self.implot=tk.Label(self.plot,image=plot_image)
        #self.implot.image=plot_image
        #self.implot.place(relx = 0.5,y = 124, anchor="center")
        check_Disease=str(predictions[np.argmax(self.ypred)])
        if(check_Disease.split("___")[1]=="healthy"):
            self.display = tk.Label(self,image=self.img)
            self.display.place(relx=0.5, y=200, anchor="center")
            self.healthy=tk.Label(text="CROP IS HEALTHY",fg="Green",font=("Times", 16),width=20)
            self.healthy.place(relx = 0.5,y = 348, anchor="center")
        else:
            self.display = tk.Label(self,image=self.img)
            self.display.place(relx=0.5, y=200, anchor="center")
            self.diseased=tk.Label(text=check_Disease.split("__")[1],fg="Black",font=("Times", 20),width=17)
            self.diseased.place(relx = 0.5,y = 348, anchor="center")
            self.link=tk.Label(text="Click For Treatment",fg="blue", cursor="hand2",font=("Times", 20),width=17)
            self.link.place(relx = 0.5,y = 380, anchor="center")
            self.url="http://www.google.com/search?q=how+to+control+"+str(predictions[np.argmax(self.ypred)])
            #print(self.url)
            self.link.bind("<Button-1>",lambda e: self.callback())
#        self.pred=tk.Label(self.result_frame,text=str(prediction),fg="#000000", bg="white", font=("Times", 32, 'bold'))
#        self.pred.place(x=450,y=150,anchor="center")

        self.hpage = tk.Button(self.result_frame, width='35', pady='7', text='BACK', bg='Green', fg='white', border=0, command=self.back)
        self.hpage.place(relx = 0.5,y = 450, anchor="center")

    def setup_loading_frame(self):
        # Create a loading frame
        self.loading_frame = tk.Frame(self, width=900, height=600, bg="white")
        self.loading_frame.place(x=0, y=0)
        
        result_img = tk.PhotoImage(file=self.main_img_path)
        self.resultbg = tk.Label(self.loading_frame, image=result_img)
        self.resultbg.image = result_img
        self.resultbg.place(x=0, y=0)

        # Create a label for the loading message
        loading_label = tk.Label(self.loading_frame,bg='#ffffff',text="Loading...", font=("Times", 20))
        loading_label.place(relx=0.5, rely=0.5, anchor="center")

        # Create a progress bar
        self.loading_progressbar = ttk.Progressbar(self.loading_frame, length=300, mode='indeterminate')
        self.loading_progressbar.place(relx=0.5, rely=0.6, anchor="center")
        self.loading_progressbar.update()
        self.loading_frame.update()
        self.process_data()

    def upload_file(self):
        f_types = [('Jpg Files', '*.JPG')]
        self.filename = filedialog.askopenfilename(filetypes=f_types)
        self.img = ImageTk.PhotoImage(file=self.filename)
        self.display = tk.Label(self,image=self.img)
        self.display.place(relx=0.5, y=320, anchor="center")
        
        
    def submit(self):
        if self.img == None:
            messagebox.showwarning("Please uplaod an Image.")
            return
        # Show the loading frame
        self.setup_loading_frame()


    def process_data(self):
        loaded_model = keras.saving.load_model("new_model.h5")
        #print(self.img.shape())
        test = Image.open(self.filename)
        # Resize the image to 256x256 pixels
        test = test.resize((256, 256))
        # Convert the image to a numpy array
        img_array = tensorflow.keras.preprocessing.image.img_to_array(test)
        # Expand the dimensions to create a batch dimension
        img_array = tensorflow.expand_dims(img_array, axis=0)
        #print(img_array.shape())
        self.ypred=loaded_model.predict(img_array)
        self.loading_frame.destroy()
        self.setup_result_frame()

    def back(self):
        try:
            self.healthy.destroy()
        except:
            self.diseased.destroy()
            self.link.destroy()
            print("done")
        self.display.destroy()        
        self.plot.destroy()
        self.resultbg.destroy()
        self.hpage.destroy()
if __name__ == "__main__":
    app = CropDiseasePrediction()
    app.mainloop()
