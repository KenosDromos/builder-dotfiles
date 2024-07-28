from dataclasses import dataclass
from typing import Optional, Generic, TypeVar, List, Tuple, Any

# T = TypeVar('T')


# @dataclass
# class Vector2(Generic[T]):
#     x: T
#     y: T

#     def get(self) -> Tuple[T, T]:
#         return (self.x, self.y)
    
#     def set(self, x: T, y: T):
#         self.x = x
#         self.y = y

#     def add(self, other: Optional['Vector2[T]']) -> 'Vector2[T]':
#         if other is None:
#             return self
#         return Vector2(self.x + other.x, self.y + other.y)

#     def subtract(self, other: Optional['Vector2[T]']) -> 'Vector2[T]':
#         if other is None:
#             return self
#         return Vector2(self.x - other.x, self.y - other.y)

#     def __str__(self):
#         return f"Vector2({self.x}, {self.y})"


# @dataclass
# class BBox(Generic[T]):
#     min: T
#     max: T

#     def get(self) -> Tuple[T, T]:
#         return (self.min, self.max)
    
#     def set(self, min: T, max: T):
#         self.min = min
#         self.max = max

#     def __str__(self):
#         return f"BBox({self.min}, {self.max})"


@dataclass
class Vector2:
    x: int
    y: int

@dataclass
class BBox:
    min: int
    max: int
