"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_ids):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagon_ids)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_two, rest = each_wagons_id[:2], each_wagons_id[2:]
    new_list = rest + first_two

    # Find the index of the locomotive (ID 1)
    loco_index = new_list.index(1)

    # Insert the missing wagons after the locomotive
    final_list = new_list[:loco_index + 1] + missing_wagons + new_list[loco_index + 1:]

    return final_list


def add_missing_stops(routing, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    ordered_stops = [stops[k] for k in sorted(stops)]
    routing['stops'] = ordered_stops
    return routing


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    
    # Merge both dictionaries
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    
    # Unpack rows
    row1, row2, row3 = wagons_rows
    # Transpose using zip to get proper columns
    fixed_rows = [list(t) for t in zip(row1, row2, row3)]
    return fixed_rows
