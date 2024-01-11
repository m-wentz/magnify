<div align="center">
<pre>
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⢉⣉⣉⣉⡉⠛⠷⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣠⣴⣿⣿⣿⣿⣿⡿⣿⣶⣌⠹⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠉⠻⣧⠘⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⠀⢹⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⠛⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⢿⡆⠈⠛⠻⠟⠛⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣦⠀⠀⠈⠉⠛⠓⠲⠶⠖⠚⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠁                                  <br>
---
capture screenshots of suspected phishing domains
</pre>
<!-- License badge -->
<a href="https://opensource.org/licenses/MIT">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</a>
</div>
<!-- Description -->
<div>
<p>A Python-based CLI tool designed to automate the process of taking screenshots of web pages using Selenium, particularly focusing on domains that might be involved in typosquatting or phishing activities. This tool is tailored towards security professionals, digital forensics experts, or anyone interested in identifying potentially malicious web pages.</p>
</div>
<!-- Features -->
<div>
<h2>Features</h2>
<ul>
<li><strong>Docker Integration:</strong> The included Dockerfile provides a secure and isolated environment for web scraping. Minimizing the risk to the host system when querying potentially malicious domains.</li>
<li><strong>Automated Screenshot Capture:</strong> Captures and saves screenshots of web pages from provided domain lists automatically.</li>
<li><strong>Headless Browsing:</strong> Supports headless mode for operations without a graphical user interface.</li>
</ul>
</div>
<!-- Prerequisites -->
<div>
<h2>Prerequisites</h2>
<ul>
<li>Python 3.x</li>
<li>pip (Python package manager)</li>
</ul>
</div>
<!-- Installation -->
<div>
<h2>Installation</h2>
<ol>
<li>
<strong>Clone This Repository:</strong>
<pre><code>git clone https://github.com/m-wentz/magnify</code></pre>
</li>
<li>
<strong>Navigate to the App Directory:</strong>
<pre><code>cd magnify</code></pre>
</li>
<li>
<strong>Install Required Packages:</strong>
<pre><code>pip install -r requirements.txt</code></pre>
</li>
</ol>
</div>
<!-- Usage -->
<div>
<h2>Usage</h2>
<p>To use <code>magnify.py</code>, follow these steps:</p>
<ol>
<li><strong>Prepare your domain list:</strong> Create a text file containing the list of domains you want to take screenshots of using a tool like <a href="https://github.com/elceef/dnstwist">DNSTwist</a>, one domain per line.</li>
<li><strong>Run the script:</strong> Use the command line to run the script with the necessary arguments. Here's the basic syntax:
<pre><code>python magnify.py -f [path_to_domain_list_file] -o [output_directory]</code></pre>
Replace <code>[path_to_domain_list_file]</code> with the path to your domain list file, and <code>[output_directory]</code> with the path where you want the screenshots to be saved.
</li>
<li><strong>Headless mode:</strong> If you want to run the browser in headless mode (without GUI), add the <code>--headless</code> flag:
<pre><code>python magnify.py -f [path_to_domain_list_file] -o [output_directory] --headless</code></pre>
</li>
</ol>
<p>Here's an example command:</p>
<pre><code>python magnify.py -f domains.txt -o screenshots</code></pre>
<p>This command will take screenshots of the domains listed in <code>domains.txt</code> and save them in a folder named <code>screenshots</code>. For additional help and a list of all command-line options, run <code>python magnify.py -h</code> or <code>python magnify.py --help</code>.</p>
</div>
<!-- Docker Integration -->
<div>
<h2>Running with Docker (Optional)</h2>
<p>This project includes a Dockerfile for easy setup and execution in a Docker container. Here's how to use it:</p>
<ol>
<li><strong>Build the Docker Image</strong>: Navigate to the directory containing the Dockerfile and run the following command to build the Docker image:</li>
<pre><code>docker build -t magnify .</code></pre>
<p>This command creates an image named <code>magnify</code>.</p>
<li><strong>Run the Container</strong>: After building the image, run the container using:</li>
<pre><code>docker run -v $(pwd)/screenshots:/usr/src/app/screenshots magnify -f /path/to/your/domain_list.txt</code></pre>
<ul>
<li>The <code>-v $(pwd)/screenshots:/usr/src/app/screenshots</code> argument mounts a local directory (<code>screenshots</code>) to the container so that the screenshots can be accessed from your host machine.</li>
<li>Replace <code>/path/to/your/domain_list.txt</code> with the actual path to your domain list file inside the container.</li>
<li>If running in headless mode, add <code>--headless</code> to the end of the command.</li>
</ul>
<p>Make sure your domain list file is accessible within the Docker container. You might need to adjust the file paths or use additional volume mounts as necessary.</p>
</ol>
</div>
<!-- Footer -->
<div>
<h2>Contributing</h2>
<p>Welcoming any contributions to this project. Here's how you can contribute:</p>
<ul>
<li>Fork the repository and create your branch from <code>main</code>.</li>
<li>Make your changes, ensuring they are well-documented and tested.</li>
<li>Submit a pull request with a clear description of your updates.</li>
</ul>
<p>Thanks for your interest in improving this project!</p>
<h2>Let's Connect!</h2>
<p>
  <a href="https://www.linkedin.com/in/m-wentz"><img src="https://github.com/gauravghongde/social-icons/blob/master/SVG/White/LinkedIN_white.svg" alt="LinkedIn"></a>
  <a href="https://github.com/m-wentz"><img src="https://github.com/gauravghongde/social-icons/blob/master/SVG/White/Github_white.svg" alt="GitHub"></a>
</p>
</div>
