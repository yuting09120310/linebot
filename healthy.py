import json
import os
import random
import re
from urllib import parse, request
import psycopg2
import requests
from bs4 import BeautifulSoup


def record(keyword):
    return "測試"