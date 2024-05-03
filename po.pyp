import c4d
import random
import math
from c4d.utils import GeRayCollider

# Be sure to use a unique ID obtained from www.plugincafe.com
# PLUGIN_ID = 1063132

	

class PineMintSunShader(c4d.plugins.ShaderData):

    def __init__(self):
        # If a Python exception occurs during the calculation of a pixel colorize this one in red for debugging purposes
        self.SetExceptionColor(c4d.Vector(1, 0, 0))
        
    def Output(self, sh, cd):
        if cd.vd:
            # Get the surface normal at the shaded point
            normal = cd.vd.n
            occlusion = 0.0

            # Number of rays to cast for ambient occlusion
            num_samples = 64

            # Iterate over rays and check for intersections
            for _ in range(num_samples):
                # Randomly sample a direction
                direction = c4d.Vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
                direction.Normalize()

                # Cast a ray from the shaded point in the sampled direction
                ray = c4d.utils.Ray(cd.vd.p, direction)
                ray.MaxDist = 100.0  # Adjust the maximum distance

                # Check for intersections
                result = cd.vd.TraceGeometry(ray)
                if result["hit"]:
                    occlusion += 1.0  # Increase occlusion factor if there is an intersection

            # Calculate the ambient occlusion value based on the number of occluded rays
            occlusion = num_samples

            return c4d.Vector(occlusion)

        return c4d.Vector(0.0)

if __name__ == '__main__':
    # Register the PineMintSunShader
    c4d.plugins.RegisterShaderPlugin(1063132, "PineMintSun", 0, PineMintSunShader, "", 0)

