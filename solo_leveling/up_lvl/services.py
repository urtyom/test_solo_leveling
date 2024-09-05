def assign_prize_to_player(player, level):
    try:
        player_level = PlayerLevel.objects.get(player=player, level=level, is_completed=True)
    except PlayerLevel.DoesNotExist:
        raise ValueError("Уровень не пройден или не существует.")

    prize = LevelPrize.objects.filter(level=level).first()
    if prize:
        player_level.prize = prize
        player_level.save()
        return f"Приз '{prize.title}' успешно присвоен игроку {player.player_id} за уровень {level.title}."
    else:
        return f"Приз за уровень {level.title} не найден."
