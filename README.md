 # social_network_task User - Post API on Django

**How to install & run?**

<ul> 
<li>git clone https://github.com/pavelrosh/social_network_task.git
/your_path/</li>
<li>cd /your_path/</li>
<li>python3 -m venv venv</li>
<li>source venv/bin/activate</li>
<li>pip install -r requirements</li>
<li>cd Network</li>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
<li>python manage.py createsuperuser</li>
<li>python manage.py test</li>
<li>python manage.py runserver</li>
</ul>

**NOTE:**
<ul>
<li>You could use Swagger fot testing this API, accessible by /api/docs route.</li>
<li>I've implemented JWT authentication.</li>
<li>On registration step email verifying by emailhunter.co, I've done it with adding adapter class. You can check in adapter.py</li>
<li>If you need to change some settings, do it via .env file.</li>
<li>You can't see API for POST in Swagger if won't authorise there.</li>
</ul>


