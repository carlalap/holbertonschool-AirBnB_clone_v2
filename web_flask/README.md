
# AirBnB clone - Web framework


<div class="panel panel-default">
  <div class="panel-heading">
   <h3 class="panel-title">Concepts</h3>
   </div>
   <div class="panel-body">
   <p>
   <em>For this project, we expect you to look at this concept:</em>
   </p>

   <ul>
   <li>
   <a href="/concepts/865">AirBnB clone</a>
   </li>
   </ul>
   </div>
  </div>


  <div class="panel panel-default" id="project-description">
  <div class="panel-body">
  <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/qk3bO45DSY-P4qmdnEX93w" title="What is a Web Framework?" target="_blank">What is a Web Framework?</a> </li>
<li><a href="/rltoken/DCF-0NHTuXLykc1ijX5HVg" title="A Minimal Application" target="_blank">A Minimal Application</a> </li>
<li><a href="/rltoken/mfdHqOmCsS7veXQ3nK6PcQ" title="Routing" target="_blank">Routing</a> (<em>except &ldquo;HTTP Methods&rdquo;</em>)</li>
<li><a href="/rltoken/_dU2691FhIZB3lBtSF5nMg" title="Rendering Templates" target="_blank">Rendering Templates</a> </li>
<li><a href="/rltoken/V24BEPWuJb3yPZpOvA3-Zw" title="Synopsis" target="_blank">Synopsis</a> </li>
<li><a href="/rltoken/GKvdWdthYkstOwnDs9LJWg" title="Variables" target="_blank">Variables</a> </li>
<li><a href="/rltoken/qum7hVpPWLaqMZBQCpcRyA" title="Comments" target="_blank">Comments</a> </li>
<li><a href="/rltoken/LxOb-5Fe9bHvx0TguTDY9g" title="Whitespace Control" target="_blank">Whitespace Control</a> </li>
<li><a href="/rltoken/8D9OoDX5cYQOFXUqwAiCNw" title="List of Control Structures" target="_blank">List of Control Structures</a> (<em>read up to &ldquo;Call&rdquo;</em>)</li>
<li><a href="/rltoken/OMqE9vlalgkWcT_3fu4Hvg" title="Flask" target="_blank">Flask</a> </li>
<li><a href="/rltoken/L3kYnmfrbc86Asb4JZq0rg" title="Jinja" target="_blank">Jinja</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/lVg3jl6IEzhNeQiHwhC-Fg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions&hellip;)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.-)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>HTML/CSS Files</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your code should be W3C compliant and validate with <a href="/rltoken/BABHSFrobycuS0xRtRtXVQ" title="W3C-Validator" target="_blank">W3C-Validator</a> (except for jinja template)</li>
<li>All your CSS files should be in the <code>styles</code> folder</li>
<li>All your images should be in the <code>images</code> folder</li>
<li>You are not allowed to use <code>!important</code> or <code>id</code> (<code>#...</code> in the CSS file)</li>
<li>All tags must be in uppercase</li>
<li>Current screenshots have been done on <code>Chrome 56.0.2924.87</code>. </li>
<li>No cross browsers </li>
</ul>

<h2>More Info</h2>

<h3>MySQL Default charset issues</h3>

<ul>
<li>If you get Flask errors after executing the  <code>curl ...</code> commands, it might be because of the <code>DEFAULT CHARSET</code>. If it&rsquo;s <code>DEFAULT CHARSET=latam1</code>, you might want to change it to <code>DEFAULT CHARSET=utf8mb4</code>, either on the server&rsquo;s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.</li>
</ul>

<h3>Install Flask</h3>

<pre><code>$ pip3 install Flask
</code></pre>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step3.png" alt="" loading='lazy' style="" /></p>

  </div>
</div>

<h2 class="gap">Tasks</h2>

   <div data-role="task19555" data-position="1" id="task-num-0">
   <div class="panel panel-default task-card " id="task-19555">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      0. Hello Flask!
    </h3>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <!-- Task Body -->
   <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo &quot;&quot; | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
</code></pre>

  </div>

<div class="list-group">
   <!-- Task URLs -->

   <!-- Github information -->
   <div class="list-group-item">
   <p><strong>Repo:</strong></p>
   <ul>
   <li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
   <li>Directory: <code>web_flask</code></li>
   <li>File: <code>0-hello_route.py, __init__.py</code></li>
   </ul>
   </div>


<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      1. HBNB
   </h3>

  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo &quot;&quot; | cat -e
HBNB$
guillaume@ubuntu:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      2. C is fun!
    </h3>
   </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo; followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo &quot;&quot; | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo &quot;&quot; | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      3. Python is cool!
    </h3>
  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo &quot;&quot; | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo &quot;&quot; | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo &quot;&quot; | cat -e
Python is cool$
guillaume@ubuntu:~$ 
</code></pre>

  </div>


<div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      4. Is it a number?
   </h3>

  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo &quot;&quot; | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
   <h3 class="panel-title">
      5. Number template
    </h3>

  </div>

  <div class="panel-body">
   <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 89&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

  </div>
