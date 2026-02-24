from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, LeaderboardEntry, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Cleared existing data.')

        # Create Users (superheroes)
        users_data = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'password': 'webslinger123'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'password': 'jarvis456'},
            {'name': 'Black Widow', 'email': 'blackwidow@marvel.com', 'password': 'natasha789'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'password': 'darknight123'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'password': 'amazonian456'},
            {'name': 'The Flash', 'email': 'flash@dc.com', 'password': 'speedforce789'},
        ]

        users = {}
        for ud in users_data:
            user = User.objects.create(**ud)
            users[ud['name']] = user
            self.stdout.write(f'Created user: {user.name}')

        # Create Teams
        marvel_team = Team.objects.create(name='Team Marvel')
        marvel_team.members.set([users['Spider-Man'], users['Iron Man'], users['Black Widow']])
        marvel_team.save()

        dc_team = Team.objects.create(name='Team DC')
        dc_team.members.set([users['Batman'], users['Wonder Woman'], users['The Flash']])
        dc_team.save()

        self.stdout.write('Created Team Marvel and Team DC.')

        # Create Activities
        activities_data = [
            {'user': users['Spider-Man'], 'activity_type': 'Web Slinging', 'duration': 45.0, 'date': date(2024, 1, 15)},
            {'user': users['Iron Man'], 'activity_type': 'Flight Training', 'duration': 60.0, 'date': date(2024, 1, 15)},
            {'user': users['Black Widow'], 'activity_type': 'Combat Training', 'duration': 90.0, 'date': date(2024, 1, 16)},
            {'user': users['Batman'], 'activity_type': 'Parkour', 'duration': 75.0, 'date': date(2024, 1, 16)},
            {'user': users['Wonder Woman'], 'activity_type': 'Sword Training', 'duration': 60.0, 'date': date(2024, 1, 17)},
            {'user': users['The Flash'], 'activity_type': 'Speed Running', 'duration': 30.0, 'date': date(2024, 1, 17)},
        ]

        for ad in activities_data:
            activity = Activity.objects.create(**ad)
            self.stdout.write(f'Created activity: {activity.activity_type} for {activity.user.name}')

        # Create Leaderboard entries
        leaderboard_data = [
            {'user': users['Spider-Man'], 'score': 950},
            {'user': users['Iron Man'], 'score': 900},
            {'user': users['Black Widow'], 'score': 870},
            {'user': users['Batman'], 'score': 920},
            {'user': users['Wonder Woman'], 'score': 880},
            {'user': users['The Flash'], 'score': 990},
        ]

        for ld in leaderboard_data:
            entry = LeaderboardEntry.objects.create(**ld)
            self.stdout.write(f'Created leaderboard entry: {entry.user.name} - {entry.score}')

        # Create Workouts
        workouts_data = [
            {
                'name': 'Hero Strength Training',
                'description': 'Full body strength workout for superheroes',
                'exercises': 'Push-ups, Pull-ups, Squats, Deadlifts, Bench Press',
            },
            {
                'name': 'Agility Circuit',
                'description': 'Speed and agility workout to enhance reflexes',
                'exercises': 'Ladder Drills, Box Jumps, Sprint Intervals, Cone Drills',
            },
            {
                'name': 'Endurance Challenge',
                'description': 'Build stamina like a true hero',
                'exercises': 'Long Distance Run, Swimming, Cycling, Row Machine',
            },
            {
                'name': 'Combat Conditioning',
                'description': 'Combat-specific fitness for crime-fighting',
                'exercises': 'Shadowboxing, Sparring, Grappling Drills, Core Work',
            },
        ]

        for wd in workouts_data:
            workout = Workout.objects.create(**wd)
            self.stdout.write(f'Created workout: {workout.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with superhero test data!'))
