from CircleCylinderClass import cylinder

def main():
    circle = cylinder(4,"Blue", 7)
    print(f"Radius is {circle.getradius()}")
    print(f"Height is {circle.getheight()}")
    print(f"Color is{circle.getcolor()}")
    print(f"Area is {'{:.2f}'.format(circle.getarea())}")
    print(f"Volume is {'{:.2f}'.format(circle.getvolume())}")

    radius_new = float(input("Set new radius (in numbers): "))
    height_new = float(input("Set new height (in numbers): "))
    color_new = str(input("Set new color: "))

    circle.setradius(radius_new)
    circle.setheight(height_new)
    circle.setcolor(color_new)

    print(f"new attributes are: radius {circle.getradius()}, height {circle.getheight()} , color {circle.getcolor()}, area {circle.getArea():.2f}, volume {circle.getvolume():.2f} ")

main()