from typing import Literal, Optional
from pydantic import BaseModel, Field
from enum import Enum

class ImpactModel(BaseModel):
    carbon_emission: float
    phosphate_production: float
    water_consumption: float
    co2_truck_km: float
    po4_laptop_hours: float
    water_bottles: float
    # level: Literal["eco", "slightly", "moderate", "heavily", "extreme"]

class DyeingInfo(BaseModel):
    country: str
    medium: Literal["article", "fabric", "yarn", None]
    weight_category: Literal[
        "extra_light",  # Extra léger < 80 g/m²
        "extra_heavy",  # Extra lourd > 400 g/m²
        "light",  # Léger 80-135 g/m²
        "heavy",  # Lourd 270-400 g/m²
        "medium",  # Moyen 135-270 g/m²
        None,
    ]

class Country(BaseModel):
    name: str
    distance: str

class Composition(BaseModel):
    material: str
    percentage: str

class Category(str, Enum):
    woven = "woven"
    knitted = "knitted"
    non_woven = "non_woven"

class Material(BaseModel):
    url: str
    name: str
    description: str
    images: list[str]
    key: str = Field(..., unique=True)
    structure: Literal[
        "denim",
        "sergé",
        "popeline",
        "jersey",
        "toile",
        "velours",
        "satin",
        "dentelle",
        "tweed",
        "twill",
        "crêpe",
        "cuir",
        "jacquard",
        "polaire",
        "interlock",
        "french terry",
        "cachemire",
        "taffetas",
        "mohair",
    ]
    category: Category
    supplier: str
    price_per_meter: float
    certifications: list[str]
    country: Country
    spinning: str
    fabrication: str
    dyeing: DyeingInfo
    composition: list[Composition]
    weight: int
    width: int
    fiber_type: Literal[
        "natural_fabrics", "synthetic_fabrics", "blended_fabrics", "recycled_fabrics"
    ]
    usage: list[
        Literal[
            "t_shirt",  # T-shirt
            "jeans",  # Jean
            "sweater",  # Pull
            "shirt",  # Chemise
            "pants",  # Pantalon
            "jacket",  # Veste
            "skirt",  # Jupe
            "dress",  # Robe
            "shorts",  # Short
            "polo",  # Polo
            "coat",  # Manteau
            "socks",  # Chaussettes
            "boxer_briefs_knit",  # Boxer / Slip (tricoté)
            "boxer_shorts_woven",  # Caleçon (tissé)
            "swimsuit",  # Maillot de bain
        ]
    ]
    colors: list[str]
    pattern: str
    dyeing_process: Literal["piece_dyed", "printed", "raw_pfd", "yarn_dyed"]
    treatment: Literal[
        "acid_dye", "direct_dye", "mercerize", "none", "not_dyed", "waterproof"
    ]
    care_instructions: list[str]
    minimum_order_quantity: int
    target: Literal["female", "male", "children", "adults", "all"]
    season: Literal["permanent", "fall_winter", "spring_summer"]
    eco_score: Literal["A", "B", "C", "D", "E", "F"]
    impact: Optional[ImpactModel] = None