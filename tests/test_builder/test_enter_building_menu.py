from Framework.screen.Login import login
from Framework.utils.Constants import BuildingType
from Framework.VillageManagement.Builder import check_building_page_title, enter_building_menu, get_building_data


if __name__ == "__main__":
    with login(headless=True) as sws:
        for bdType in BuildingType:
            buildings = get_building_data(sws, bdType)
            if buildings:
                for bdIndex, bdLevel in buildings:
                    assert enter_building_menu(sws, bdIndex)
                    assert check_building_page_title(sws, bdType)
