# phys.libretexts-Scraper
A scraper for the website [phys.libretexts](https://phys.libretexts.org/).
# Contributing
This project is under construction. If you want to contribute to this project create a fork and submit a PR. <br /> <br />
Also feel free to create a new [issue](https://github.com/WildCyclotron/phys.libretexts-scraper/issues) if you found a bug or have a suggestion. 
# Installing
* Make sure to get Python 3.7 or higher.
* Set up venv
```
python3.8 -m venv venv
```
* Clone this repository
```
$ git clone https://github.com/WildCyclotron/phys.libretexts-scraper.git
```
* Install dependencies
```
pip install -U -r requirements.txt
```
# Usage 
### Example  
```py
import physlibretexts

physlibretexts.search('momentum',1)
```
### Output
```json
{
  "results": [
    {
      "title": "Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Supplemental_Modules_(Classical_Mechanics)/Conservation_of_Momentum/Momentum",
      "content": "If the sun is directly overhead, the motion of the ball's shadow on the ground seems perfectly natural: there are no horizontal forces, so it either sits still or moves at constant velocity. (Zero for..."
    },
    {
      "title": "10.1: Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_Introductory_Physics_-_Building_Models_to_Describe_Our_World_(Martin_Neary_Rinaldo_and_Woodman)/10%3A_Linear_Momentum_and_the_Center_of_Mass/10.01%3A_Momentum",
      "content": "We thus have:\nd\ndt\n(\n→\np\n1+\n→\np\n2)=∑\n→\nF\next\nFurthermore, if we introduce the “total momentum of the system”,\n→\nP\n=\n→\np\n1+\n→\np\n2, as..."
    },
    {
      "title": "3.3: Moment of Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Classical_Mechanics_(Tatum)/03%3A_Systems_of_Particles/3.03%3A_Moment_of_Momentum",
      "content": "Moment of momentum plays a role in rotational motion analogous to the role played by linear momentum in linear motion, and is also called angular momentum. Several choices for expressing angular momen..."
    },
    {
      "title": "3.2: Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_I_-_Classical_Mechanics_(Gea-Banacloche)/03%3A_Momentum_and_Inertia/3.02%3A_Momentum",
      "content": "For instance, if you are driving in a car towing a trailer behind you, the trailer has only a large amount of inertia, but no momentum, relative to you, because its velocity relative to you is zero; h..."
    },
    {
      "title": "9.2: Linear Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Book%3A_University_Physics_I_-_Mechanics_Sound_Oscillations_and_Waves_(OpenStax)/09%3A_Linear_Momentum_and_Collisions/9.02%3A_Linear_Momentum",
      "content": "Momentum is a concept that describes how the motion of an object depends not only on its mass, but also its velocity. Momentum is a vector quantity that depends equally on an object's mass and velocit..."
    },
    {
      "title": "14.6: Conservation of Four-Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/University_Physics/Radically_Modern_Introductory_Physics_Text_II_(Raymond)/14%3A_Forces_in_Relativity/14.06%3A_Conservation_of_Four-Momentum",
      "content": "In other words, if we have a number of particles isolated from the rest of the universe, each with momentum pi\nand energy Ei\n, then particles may be cr..."
    },
    {
      "title": "11.3: Angular Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Book%3A_University_Physics_I_-_Mechanics_Sound_Oscillations_and_Waves_(OpenStax)/11%3A__Angular_Momentum/11.03%3A_Angular_Momentum",
      "content": "The angular momentum of a single particle about a designated origin is the vector product of the position vector in the given coordinate system and the particle’s linear momentum. The net torque on a ..."
    },
    {
      "title": "Angular Momentum",
      "link": "https://phys.libretexts.org/Courses/Joliet_Junior_College/Physics_201_-_Fall_2019/Book%3A_Physics_(Boundless)/10%3A_Rotational_Kinematics%2C_Angular_Momentum%2C_and_Energy/10.08%3A__Angular_Momentum/Angular_Momentum",
      "content": "The angular momentum of a single particle about a designated origin is the vector product of the position vector in the given coordinate system and the particle’s linear momentum. The net torque on a ..."
    },
    {
      "title": "12.3: Angular Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_Introductory_Physics_-_Building_Models_to_Describe_Our_World_(Martin_Neary_Rinaldo_and_Woodman)/12%3A_Rotational_Energy_and_Momentum/12.03%3A_Angular_Momentum",
      "content": "In this section, we show that we can define a quantity called “angular momentum” as the rotational equivalent of the linear momentum."
    },
    {
      "title": "1.5: Four-Momentum",
      "link": "https://phys.libretexts.org/Courses/Skidmore_College/Introduction_to_General_Relativity/01%3A_Special_Relativity/1.05%3A_Four-Momentum",
      "content": "In Newtonian mechanics, position in space can be indicated with a three-dimensional vector. In Special Relativity, however, events are indicated using four coordinates: x=(t,x,y,z)."
    },
    {
      "title": "7.2: Generalized Momentum",
      "link": "https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline)/07%3A_Symmetries_Invariance_and_the_Hamiltonian/7.02%3A_Generalized_Momentum",
      "content": "Introduce generalized momentum."
    }
  ]
}
```

