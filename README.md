# Squad2 - Web-based Military Unit Personnel Management System

## Project Description

Django web application for managing military unit personnel. The system provides complete functionality for staff roster management, personal records, weapons tracking, and document workflow through a web interface.

This is the web version of the [Staff](https://github.com/PopovMarko/staff) project, allowing users to work with the system through a browser without needing to install a desktop application.

## Features

- 🌐 Web interface accessible through browser
- 🔐 User authentication and authorization system
- 📊 Interactive tables and forms
- 💾 Centralized database
- 🚀 Quick access from any device on the network
- 📱 Responsive design for different screen sizes

## Technology Stack

**Backend:**
- Python 3.x
- Django 4.x - web framework
- SQLite - database

**Frontend:**
- HTML5
- CSS3
- JavaScript
- Bootstrap (possibly)

## Project Structure

```
squad2/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
├── squad2/               # Main Django app
│   ├── settings.py       # Project settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── evening/             # Evening app module
├── material/            # Material management module
├── staff.csv            # Staff data export
└── test.py              # Test scripts
```

## Key Features

### Personnel Management
- Add and edit service member information
- Maintain personal records with complete information
- Track position assignments
- Service activity history

### Staff Roster
- Create and manage unit staff structure
- Display vacant and filled positions
- Appointment and dismissal management
- View unit staffing levels

### Weapons Tracking
- Personal weapons registry
- Weapon assignment to service members
- Weapon issuance and return history
- Accountability control

### Document Management
- Electronic document copy storage
- Passports, military IDs, combat participant certificates
- Appointment and discharge orders
- Family member records

### Leave Management
- Leave planning and tracking
- Used days control
- Individual leave history

## Installation and Setup

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/PopovMarko/squad2.git
cd squad2
```

### Step 2: Create Virtual Environment

**For Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations (first run)

```bash
python manage.py migrate
```

### Step 5: Create Superuser (optional)

```bash
python manage.py createsuperuser
```

Enter username, email, and password for the administrator.

### Step 6: Run the Server

```bash
python manage.py runserver 8080
```

The server will start on port 8080.

### Step 7: Access the Application

Open your browser and navigate to:

```
http://localhost:8080/index/
```

To access Django admin panel:

```
http://localhost:8080/admin/
```

### Stop the Server

Press `Ctrl+C` in the terminal to stop the server.

### Deactivate Virtual Environment

```bash
deactivate
```

## Usage

### Home Page
- Navigate to `http://localhost:8080/index/`
- Navigation menu provides access to all sections

### Data Management
- **Adding:** Use forms to add new records
- **Editing:** Click on a record to edit
- **Deleting:** Use corresponding buttons (with confirmation)
- **Search:** Use search fields for quick information lookup

### Data Export
- CSV export available for main tables
- Saved files are located in the project root directory

## Administration

### Django Admin Panel
Access admin panel at: `http://localhost:8080/admin/`

**Capabilities:**
- User and permission management
- Direct access to all data models
- Bulk record editing
- Change log viewing

### Database Management

**Create backup:**
```bash
python manage.py dumpdata > backup.json
```

**Restore from backup:**
```bash
python manage.py loaddata backup.json
```

**Clear database:**
```bash
python manage.py flush
```

## Development

### Adding New Features

1. **Create a new model:**
```python
# in models.py
class NewModel(models.Model):
    field = models.CharField(max_length=100)
```

2. **Create migration:**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Register in admin:**
```python
# in admin.py
from .models import NewModel
admin.site.register(NewModel)
```

### Configuration

Main settings in `squad2/settings.py`:
- `DEBUG` - debug mode (True for development)
- `ALLOWED_HOSTS` - allowed hosts
- `DATABASES` - database configuration
- `STATIC_URL` - static files path

### Static Files

**Collect static files for production:**
```bash
python manage.py collectstatic
```

## Security

### Production Recommendations:

1. **Disable DEBUG mode:**
```python
DEBUG = False
```

2. **Set SECRET_KEY:**
```python
SECRET_KEY = 'your-secret-key-here'
```

3. **Configure ALLOWED_HOSTS:**
```python
ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address']
```

4. **Use HTTPS**

5. **Configure CSRF protection**

6. **Regularly update dependencies:**
```bash
pip list --outdated
pip install --upgrade package-name
```

## Deployment

### For Local Network:

1. Find your IP address:
```bash
# Linux/Mac
ifconfig
# Windows
ipconfig
```

2. Add IP to ALLOWED_HOSTS in settings.py

3. Run server on all interfaces:
```bash
python manage.py runserver 0.0.0.0:8080
```

4. Access from other computers:
```
http://YOUR-IP-ADDRESS:8080/index/
```

### For Production:

Recommended to use:
- **Gunicorn** or **uWSGI** as WSGI server
- **Nginx** as reverse proxy
- **PostgreSQL** instead of SQLite
- **Docker** for containerization

## Comparison with Desktop Version

| Feature | Desktop (staff) | Web (squad2) |
|---------|----------------|--------------|
| **Access** | Local computer | Any device on network |
| **Installation** | Required on each PC | Once on server |
| **Updates** | On each PC | Only on server |
| **Multi-user** | Limited | Full support |
| **Backup** | Local | Centralized |
| **Interface** | Desktop UI | Web interface |

## Known Limitations

- SQLite not recommended for production with many concurrent users
- Large file handling requires additional configuration
- Limited real-time update support (WebSocket needed for this)

## Future Improvements

- [ ] REST API for mobile applications
- [ ] Real-time updates via WebSockets
- [ ] Advanced reporting system
- [ ] Export to PDF and Excel
- [ ] Mobile interface version
- [ ] Active Directory integration
- [ ] Multi-language interface
- [ ] Notification system
- [ ] Charts and analytics
- [ ] PostgreSQL migration

## Troubleshooting

**"Port already in use" error:**
```bash
# Find process
lsof -i :8080
# Or use different port
python manage.py runserver 8081
```

**Migration errors:**
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

**Static files not loading:**
```bash
python manage.py collectstatic --clear
```

## Author

Popov Marko Vyacheslavovych

## License

Private project for official use

---

**Note:** This project is developed for military record-keeping purposes and contains confidential information. Usage is restricted to official needs.
