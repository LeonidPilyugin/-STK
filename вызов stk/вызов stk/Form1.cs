using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using AGI.Ui.Application;
using AGI.STK;
using AGI.STKObjects;

namespace вызов_stk
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        [DllImport(@"RunPython.dll")]
        static extern void run();
        private void button1_Click(object sender, EventArgs e)
        {
            AgUiApplication uiApplication = new AgUiApplication();
            uiApplication.LoadPersonality("STK");
            uiApplication.Visible = false;
            IAgStkObjectRoot root = uiApplication.Personality2 as IAgStkObjectRoot;
            root.NewScenario("scenario");
            IAgStar star = root.CurrentScenario.Children.New(AgESTKObjectType.eStar, "MyStar") as IAgStar;

            //wait();

            run();

            //wait();

            AgFacility facility = root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "MyFacility") as AgFacility;

            button1.Text = root.CurrentScenario.Children.Count.ToString();
            uiApplication.Quit();
        }
    }
}
