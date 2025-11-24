<p>&nbsp;</p>
<h1>Auto Git Push Tool</h1>
<p><strong>A simple Python tool to automatically push your GitHub repository at regular intervals.</strong></p>
<p>Many times, after working on a project (at school, office, or home), we forget to push our changes to GitHub. This tool automates the process, saving your work continuously and ensuring your repository stays updated.</p>
<p>You can also create an executable (<code>.exe</code>) file to run this tool easily without opening Python.</p>
<hr />
<h2>Features</h2>
<ul>
<li>
<p>Automatically detects changes in your Git repository.</p>
</li>
<li>
<p>Creates a commit with a timestamped message including changed files.</p>
</li>
<li>
<p>Pushes commits to the <code>main</code> branch of your GitHub repository.</p>
</li>
<li>
<p>Adjustable delay (in minutes) for automatic pushing.</p>
</li>
<li>
<p>GUI interface for easy usage (Tkinter-based).</p>
</li>
<li>
<p>Run silently in the background without opening a console window.</p>
</li>
<li>
<p>Compatible with Windows.</p>
</li>
</ul>
<p>Optional: Integrate <strong>Gemini API</strong> to customize commit messages further.</p>
<hr />
<h2>Usage Instructions</h2>
<ol>
<li>
<p><strong>Initial Setup</strong></p>
<ul>
<li>
<p>First, manually push your Git repository to GitHub to set the remote.</p>
</li>
</ul>
</li>
<li>
<p><strong>Launch the Tool</strong></p>
<ul>
<li>
<p>Open the tool (Python script or compiled <code>.exe</code>).</p>
</li>
<li>
<p>Browse and select your Git repository folder.</p>
</li>
<li>
<p>Set the delay time (in minutes) for how often you want auto-push to occur. Default is 3 minutes.</p>
</li>
</ul>
</li>
<li>
<p><strong>Start Auto Push</strong></p>
<ul>
<li>
<p>Click <strong>Start Auto Push</strong>.</p>
</li>
<li>
<p>The tool will automatically check for changes, commit them with a timestamp, and push to GitHub at the specified interval.</p>
</li>
</ul>
</li>
<li>
<p><strong>Stop Auto Push</strong></p>
<ul>
<li>
<p>Click <strong>Stop</strong> to halt the auto push process.</p>
</li>
</ul>
</li>
</ol>
<hr />
<h2>Notes &amp; Recommendations</h2>
<ul>
<li>
<p><strong>Avoid very short intervals</strong>: Setting too short a delay may trigger warnings from GitHub (rate-limiting or spam detection).</p>
</li>
<li>
<p><strong>Initial push required</strong>: Ensure your repository has been pushed at least once manually.</p>
</li>
<li>
<p><strong>Commit messages</strong>: By default, the commit message includes the timestamp and changed files. You can modify this or use APIs like Gemini for custom commit messages.</p>
</li>
<li>
<p><strong>Windows Only</strong>: Currently, this tool uses <code>CREATE_NO_WINDOW</code> to run Git silently, which is Windows-specific.</p>
</li>
</ul>
<hr />
<h2>Requirements</h2>
<ul>
<li>
<p>Python 3.6+</p>
</li>
<li>
<p>Git installed and added to system PATH</p>
</li>
<li>
<p>Libraries:</p>
<ul>
<li>
<p><code>tkinter</code> (usually included with Python)</p>
</li>
<li>
<p><code>subprocess</code> (built-in)</p>
</li>
<li>
<p><code>threading</code>, <code>time</code>, <code>datetime</code>, <code>os</code> (built-in)</p>
</li>
</ul>
</li>
</ul>
<hr />
<h2>How it Works</h2>
<ol>
<li>
<p>The tool monitors your selected Git repository folder.</p>
</li>
<li>
<p>It runs <code>git status</code> to detect changes.</p>
</li>
<li>
<p>If changes are found:</p>
<ul>
<li>
<p><code>git add .</code></p>
</li>
<li>
<p><code>git commit -m "[TIMESTAMP] - file1, file2..."</code></p>
</li>
<li>
<p><code>git push origin main</code></p>
</li>
</ul>
</li>
<li>
<p>Waits for the specified delay and repeats the process.</p>
</li>
</ol>
<hr />
<h2>Example Screenshot</h2>
<img width="801" height="650" alt="Image" src="https://github.com/user-attachments/assets/736cf24e-5ff6-40d4-83f2-69d9b010f3e0" />
<p>&nbsp;</p>
<hr />
<h2>Optional Enhancements</h2>
<ul>
<li>
<p><strong>Custom commit messages</strong> using APIs like Gemini.</p>
</li>
<li>
<p><strong>Cross-platform support</strong> by handling silent execution differently for Linux/Mac.</p>
</li>
<li>
<p><strong>Logging to a file</strong> to keep a persistent record of all pushes.</p>
</li>
</ul>
<hr />
<h2>License</h2>
<p>MIT License &ndash; free to use and modify.</p>
<p>&nbsp;</p>
