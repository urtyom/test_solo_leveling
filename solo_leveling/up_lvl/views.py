from django.http import HttpResponse
import csv

def export_player_levels_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="player_levels.csv"'

    writer = csv.writer(response)
    writer.writerow(['Player ID', 'Level', 'Completed', 'Prize'])

    player_levels = PlayerLevel.objects.select_related('player', 'level').prefetch_related('level__levelprize').all()

    for player_level in player_levels.iterator():
        prize = player_level.level.levelprize_set.first() if player_level.level.levelprize_set.exists() else None
        writer.writerow([
            player_level.player.player_id,
            player_level.level.title,
            "Yes" if player_level.is_completed else "No",
            prize.prize.title if prize else "No prize"
        ])

    return response
