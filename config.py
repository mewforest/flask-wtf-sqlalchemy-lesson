# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'abcdef1234567890!@#$%^000!!!'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_EMAIL = 'example@gmail.com'
    INTRO_WORDS_COUNT = 20
    LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT') or False
