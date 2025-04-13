class Nose:
    """Creates a Nose which can smell."""
    def __init__(self):
        self.smelled_smells = set()


    def get_smelled_smells(self):
        return self.smelled_smells.copy()


class HumanNose(Nose):
    """Creates a Human Nose which can smell."""
    def __init__(self, allergies=None):
        super().__init__()
        self.immune_response = False
        self.allergies = allergies or []


    def smell(self, odor):
        """
        Smell an odor.
        Humans must not have an active immune response to smell.
        """
            
        if not self.immune_response:
            if odor in self.allergies:
                self.immune_response = True
            else:
                self.smelled_smells.add(odor)
        else:
            raise RuntimeError("Nose cannot smell when immune response is active.")

    def rest(self):
        """
        Reset the immune response for humans.
        """
        self.immune_response = False


class RobotNose(Nose):
    """
    Creates a Robot Nose which can smell.
    """
    def __init__(self, air_tank_capacity_liters=20):
        super().__init__()
        self.air_tank_capacity_liters = air_tank_capacity_liters
        self.current_air_tank_level = 0

    def smell(self, odor):
        """
        Smell an odor. 
        Robots must have capacity in their air tank to smell.
        """
        if self.current_air_tank_level < self.air_tank_capacity_liters:
                self.smelled_smells.add(odor)
                self.current_air_tank_level += 1
        else:
            raise RuntimeError("Robot nose cannot smell when air tank is full.")
        

    def reset(self):
        """ Resets the robot air tank"""
        self.current_air_tank_level = 0


if __name__ == "__main__":
    print("Run `pytest tests/smells2_test.py` instead.")
