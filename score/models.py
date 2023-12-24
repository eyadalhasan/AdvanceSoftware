# Assuming you have models for User and EnvironmentalData in environmental_data/models.py

from environmental_data.models import User, EnvironmentalData


def update_sustainability_score(user_id, interaction_type):
    # Fetch the user
    user = User.objects.get(pk=user_id)

    # Check if the user already has a sustainability score
    user_score, created = Score.objects.get_or_create(user=user)

    # Increment the score for a useful interaction
    if interaction_type == 'Useful Interaction':
        user_score.sustainability_score += 1
        user_score.save()

    return user_score.sustainability_score


# Example usage:
# Assuming user_id is the ID of the user for whom you want to update the sustainability score
user_id = 1  # Replace with the actual user ID
interaction_type = 'Useful Interaction'  # Replace with the actual interaction type
updated_score = update_sustainability_score(user_id, interaction_type)
print(f"Updated Sustainability Score for User ID {user_id}: {updated_score}")
