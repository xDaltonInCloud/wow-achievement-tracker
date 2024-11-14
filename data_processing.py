class AchievementProcessor:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def process_achievements(self):
        # Extract only the relevant achievement information
        achievements = []
        
        for achievement in self.raw_data.get("achievements", []):
            achievements.append({
                "id": achievement.get("id"),
                "title": achievement.get("title"),
                "description": achievement.get("description"),
                "completed_timestamp": achievement.get("completed_timestamp"),
                "is_completed": bool(achievement.get("completed_timestamp")),
                "points": achievement.get("points")
            })
        
        return achievements

    def calculate_completion_rate(self, achievements):
        # Calculate the percentage of achievements completed
        total_achievements = len(achievements)
        completed_achievements = sum(1 for ach in achievements if ach['is_completed'])
        
        if total_achievements > 0:
            completion_rate = (completed_achievements / total_achievements) * 100
        else:
            completion_rate = 0.0
            
        return round(completion_rate, 2)
