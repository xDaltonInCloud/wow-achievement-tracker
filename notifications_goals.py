class GoalTracker:
    def __init__(self, achievements):
        self.achievements = achievements

    def set_goal(self, target_completion_rate):
        self.target_completion_rate = target_completion_rate

    def check_goal(self, current_completion_rate):
        if current_completion_rate >= self.target_completion_rate:
            return True  # Goal reached
        return False

def send_notification(goal_reached, character_name):
    if goal_reached:
        print(f"Congratulations! {character_name} has reached the goal completion rate!")
    else:
        print(f"Keep going! You’re almost there.")
