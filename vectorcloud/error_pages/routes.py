#!/usr/bin/env python3

from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

# ------------------------------------------------------------------------------
# Error Pages
# ------------------------------------------------------------------------------


@error_pages.route("/vector_not_found")
def vector_not_found():
    return render_template('/error_pages/vector_not_found.html')


@error_pages.route("/vector_stuck")
def vector_stuck():
    return render_template('/error_pages/vector_stuck.html')


@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('/error_pages/404.html'), 404


@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('/error_pages/403.html'), 403


@error_pages.app_errorhandler(500)
def error_500(error):
    return render_template('/error_pages/500.html'), 500