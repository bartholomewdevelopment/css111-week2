import math

def compute_volume(radius_cm, height_cm):
    """Return the volume of a cylinder (steel can) in cubic centimeters."""
    return math.pi * (radius_cm ** 2) * height_cm

def compute_surface_area(radius_cm, height_cm):
    """Return the exterior surface area of a cylinder in square centimeters."""
    return 2 * math.pi * radius_cm * (radius_cm + height_cm)

def compute_storage_efficiency(radius_cm, height_cm):
    """Return storage efficiency = volume / surface_area."""
    vol = compute_volume(radius_cm, height_cm)
    sa = compute_surface_area(radius_cm, height_cm)
    return vol / sa

def compute_cost_efficiency(radius_cm, height_cm, cost_usd):
    """Return cost efficiency = volume / cost (cm^3 per USD)."""
    vol = compute_volume(radius_cm, height_cm)
    return vol / cost_usd

def main():
    # Data: (Name, Radius (cm), Height (cm), Cost (USD))
    cans = [
        ("#1 Picnic",   6.83, 10.16, 0.28),
        ("#1 Tall",     7.78, 11.91, 0.43),
        ("#2",          8.73, 11.59, 0.45),
        ("#2.5",       10.32, 11.91, 0.61),
        ("#3 Cylinder",10.79, 17.78, 0.86),
        ("#5",         13.02, 14.29, 0.83),
        ("#6Z",         5.40,  8.89, 0.22),
        ("#8Z short",   6.83,  7.62, 0.26),
        ("#10",        15.72, 17.78, 1.53),
        ("#211",        6.83, 12.38, 0.34),
        ("#300",        7.62, 11.27, 0.38),
        ("#303",        8.10, 11.11, 0.42),
    ]

    # Headers
    print("Name".ljust(12),
          "Radius(cm)".rjust(11),
          "Height(cm)".rjust(11),
          "Volume(cm^3)".rjust(14),
          "SurfArea(cm^2)".rjust(16),
          "StorEff(V/SA)".rjust(14),
          "Cost($)".rjust(8),
          "CostEff(V/$)".rjust(14),
          sep="  ")
    print("-" * 112)

    best_storage = (None, float("-inf"))  # (name, storage_efficiency)
    best_cost = (None, float("-inf"))     # (name, cost_efficiency)

    for name, r, h, cost in cans:
        vol = compute_volume(r, h)
        sa = compute_surface_area(r, h)
        storage_eff = vol / sa if sa != 0 else 0.0
        cost_eff = compute_cost_efficiency(r, h, cost)

        # Track bests
        if storage_eff > best_storage[1]:
            best_storage = (name, storage_eff)
        if cost_eff > best_cost[1]:
            best_cost = (name, cost_eff)

        # Print row
        print(
            name.ljust(12),
            f"{r:>11.2f}",
            f"{h:>11.2f}",
            f"{vol:>14.2f}",
            f"{sa:>16.2f}",
            f"{storage_eff:>14.5f}",
            f"${cost:>6.2f}",
            f"{cost_eff:>14.2f}",
            sep="  "
        )

    print("\nSummary:")
    print(f"- Highest storage efficiency: {best_storage[0]} ({best_storage[1]:.5f})")
    print(f"- Highest cost efficiency:    {best_cost[0]} ({best_cost[1]:.2f} cm^3 per $)")

if __name__ == "__main__":
    main()
