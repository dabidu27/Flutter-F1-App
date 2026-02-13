from datetime import datetime, timedelta, timezone


def getSecondsUntilRaceFinish(nextRaceIso):

    try:

        raceStart = datetime.fromisoformat(nextRaceIso.replace("Z", "+00:00"))
        raceFinish = raceStart + timedelta(hours=2, minutes=30)

        now = datetime.now(timezone.utc)
        remaining = (raceFinish - now).total_seconds()

        return int(remaining)

    except:
        return 3600
