using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;

namespace morseCodeDecoder
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnRnPython_Click(object sender, EventArgs e)
        {
            try
            {
                string appDir = AppDomain.CurrentDomain.BaseDirectory;
                string projectRoot = Directory.GetParent(appDir).Parent.Parent.FullName;
                string pythonExe = Path.Combine(projectRoot,
                                                "pythonApp",
                                                "venv",
                                                "Scripts",
                                                "python.exe");
                string scriptPath = Path.Combine(projectRoot,
                                                "PythonApp",
                                                "main.py");

                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = pythonExe,
                    Arguments = $"\"{scriptPath}\"",
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using (Process process = new Process())
                {
                    process.StartInfo = psi;

                    process.OutputDataReceived += (s, ev) =>
                    {
                        if (ev.Data != null && ev.Data.StartsWith("[MSG]"))
                        {
                            string msg = ev.Data.Substring(5);
                            this.Invoke((Action)(() =>
                            {
                                lblOutput.Text = msg;
                            }));
                        }
                    };
                    process.Start();
                    process.BeginOutputReadLine();
                }
            }
            catch (Exception ex)
            {
                lblOutput.Text = $"Exception: \n{ex.Message}";
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            DialogResult res =
                MessageBox.Show("Are you sure?",
                                "Exit",
                                MessageBoxButtons.YesNoCancel,
                                MessageBoxIcon.Question);
            if (res == DialogResult.Yes) 
            {
                Application.Exit();
            }
        }

        private void pictureBox1_MouseEnter(object sender, EventArgs e)
        {
            pictureBox1.Cursor = Cursors.Hand;
            pictureBox1.BackColor = Color.Gray;
        }

        private void pictureBox1_MouseLeave(object sender, EventArgs e)
        {
            pictureBox1.Cursor = Cursors.Default;
            pictureBox1.BackColor = Color.Transparent;
        }
    }
}
