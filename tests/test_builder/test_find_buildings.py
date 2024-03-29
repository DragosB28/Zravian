from Framework.screen.Login import login
from Framework.utils.Constants import BuildingType, get_BUILDINGS
from Framework.VillageManagement.Builder import find_building

BUILDINGS = get_BUILDINGS()


if __name__ == "__main__":
    with login(headless=True) as driver:
        # Requires manual checking
        for bdType in BuildingType:
            if bdType != BuildingType.EmptyPlace:
                print(f'{BUILDINGS[bdType].name}: {find_building(driver, bdType)}')
