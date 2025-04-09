from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create and save users individually
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='password123'),
            User(email='zerocool@mhigh.edu', name='Elliot Alderson', password='password123'),
            User(email='crashoverride@mhigh.edu', name='Dade Murphy', password='password123'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', password='password123'),
        ]
        for user in users:
            user.save()

        # Create and save teams individually
        teams = [
            Team(name='Blue Team', members=[user.email for user in users[:3]]),
            Team(name='Gold Team', members=[user.email for user in users[3:]]),
        ]
        for team in teams:
            team.save()

        # Create and save activities individually
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, date=date.today()),
            Activity(user=users[1], activity_type='Crossfit', duration=120, date=date.today()),
            Activity(user=users[2], activity_type='Running', duration=90, date=date.today()),
            Activity(user=users[3], activity_type='Strength', duration=30, date=date.today()),
            Activity(user=users[4], activity_type='Swimming', duration=75, date=date.today()),
        ]
        for activity in activities:
            activity.save()

        # Create and save leaderboard entries individually
        leaderboard_entries = [
            Leaderboard(team=teams[0], points=100),
            Leaderboard(team=teams[1], points=90),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Create and save workouts individually
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
