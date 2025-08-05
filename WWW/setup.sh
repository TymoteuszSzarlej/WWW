#!/bin/bash

# Create main project template
mkdir -p _templates
cat > _templates/base.html << 'EOL'
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}RavaDev{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    <link rel="icon" href="{% static 'img/favicon.ico' %}">
    <script src="https://kit.fontawesome.com/yourkit.js" crossorigin="anonymous"></script>
    {% block head %}{% endblock %}
</head>
<body style="background: var(--bg-color); color: var(--text-color);">
    <header>
        <nav class="navbar" aria-label="Główna nawigacja">
            <a href="{% url 'index' %}" class="logo" aria-label="Strona główna">RavaDev</a>
            <ul>
                <li><a href="{% url 'service_list' %}">Usługi</a></li>
                <li><a href="{% url 'finished_projects' %}">Portfolio</a></li>
                <li><a href="{% url 'blog_index' %}">Blog</a></li>
                <li><a href="{% url 'subscription_list' %}">Subskrypcje</a></li>
                <li><a href="{% url 'contact:start_conversation' %}" class="btn">Kontakt</a></li>
                {% if user.is_authenticated %}
                    <li><a href="{% url 'settings' %}">Moje konto</a></li>
                    <li><a href="{% url 'logout' %}">Wyloguj</a></li>
                {% else %}
                    <li><a href="{% url 'login' %}">Logowanie</a></li>
                {% endif %}
            </ul>
        </nav>
        {% block header %}{% endblock %}
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <div class="footer-content">
            <p>&copy; {{ year|default:2025 }} RavaDev. Wszelkie prawa zastrzeżone.</p>
            <ul class="social-links">
                <li><a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a></li>
                <li><a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a></li>
                <li><a href="#" aria-label="GitHub"><i class="fab fa-github"></i></a></li>
            </ul>
        </div>
    </footer>
    <script src="{% static 'js/main.js' %}"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
EOL

# Create base templates for each app
create_base_template() {
  app=$1
  mkdir -p "_templates/${app}"
  cat > "_templates/${app}/base_${app}.html" << EOL
{% extends "base.html" %}

{% block title %}{{ app|title }} | RavaDev{% endblock %}

{% block content %}
<div class="${app}-container">
    {% block ${app}_content %}{% endblock %}
</div>
{% endblock %}
EOL
}

create_base_template users
create_base_template subscriptions
create_base_template services
create_base_template index
create_base_template contact
create_base_template blog

# Function to create view templates
create_view_template() {
  app=$1
  template=$2
  mkdir -p "_templates/${app}"
  cat > "_templates/${app}/${template}.html" << EOL
{% extends "${app}/base_${app}.html" %}

{% block ${app}_content %}
<!-- ${app}/${template}.html content -->
{% endblock %}
EOL
}

# Users templates
create_view_template users register
create_view_template users login
create_view_template users password_reset
create_view_template users settings

# Subscriptions templates
create_view_template subscriptions list
create_view_template subscriptions buy
create_view_template subscriptions extend
create_view_template subscriptions delete
create_view_template subscriptions success
create_view_template subscriptions cancel

# Services templates
create_view_template services list
create_view_template services detail
create_view_template services free_valuation
create_view_template services schedule_meeting

# Index templates
create_view_template index index
create_view_template index team
create_view_template index clients
create_view_template index projects

# Contact templates
create_view_template contact start_conversation
create_view_template contact conversation_detail
create_view_template contact send_message
create_view_template contact add_lead

# Blog templates
create_view_template blog index
create_view_template blog category_posts
create_view_template blog post_detail
create_view_template blog add_comment
create_view_template blog add_review

echo "All templates created successfully!"
