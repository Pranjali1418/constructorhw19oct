# Create constructor and objects of GymMembership class

class GymMembership:
    def __init__(self, member_name, membership_days):
        print(f"GymMembership constructor is running for {member_name}")
        self.member_name = member_name
        self.membership_days = membership_days

gym1 = GymMembership("Omkar", 30)
gym2 = GymMembership("Pranjali", 60)

print(gym1.membership_days)

gym1.membership_days = 60

print("Updated attributes are :")
print(gym1.membership_days)
print(gym2.member_name)