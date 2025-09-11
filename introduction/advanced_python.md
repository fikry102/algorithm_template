# Python高阶语法（选看）

## 1. 生成器 (Generators) — 懒加载，高效率 🐢⚡

生成器是"懒惰的工人"，只在需要时才工作，内存友好。

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # 使用 yield，不是 return
        count += 1

# 用法
gen = count_up_to(5)
for num in gen:
    print(num)  # 输出 1, 2, 3, 4, 5
```

**特点：**
- 内存高效，适合大数据集
- 使用 `yield` 暂停和恢复执行
- 可以与 `next()`, `send()` 配合实现协程行为

## 2. 描述符 (Descriptors) — @property 的内部机制

描述符是Python属性访问的核心机制，控制属性的赋值和读取。

```python
class Positive:
    def __init__(self):
        self.name = None
    
    def __set_name__(self, owner, name):
        # Python 3.6+ 自动调用，记录属性名
        self.name = name
    
    def __get__(self, instance, owner):
        # 读取属性时调用
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        # 赋值时调用，可以加校验
        if value <= 0:
            raise ValueError("值必须为正数")
        instance.__dict__[self.name] = value

class Account:
    balance = Positive()  # 余额必须为正数

# 使用
a = Account()
a.balance = 100  # OK
# a.balance = -50  # 抛出异常
```

**核心方法：**
- `__get__`：属性读取时触发
- `__set__`：属性赋值时触发
- `__set_name__`：描述符绑定到类属性时自动调用

**用途：**
- 属性校验（如余额必须为正数）
- 计算属性
- 访问日志记录

## 3. 元类 (Metaclasses) — Python的终极Boss 😈

元类控制"类"的创建过程，是"类的工厂"。

```python
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f'正在创建类: {name}')
        # 可以在这里修改类的属性或方法
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass  # 创建时会打印 "正在创建类: MyClass"
```

**核心概念：**
- `type` 是Python的默认元类
- `__new__` 参数：
  - `cls`：元类本身
  - `name`：新类的名字
  - `bases`：基类
  - `attrs`：类的属性字典

**实际应用：**
- 框架开发（Django ORM、SQLAlchemy）
- 自动注册类
- 强制类约束
- 在类创建时注入方法

## 4. 装饰器进阶 — 装饰器的装饰器

装饰器是函数的"外套"，给函数增加功能而不修改原代码。

```python
from functools import wraps

def smart_decorator(func):
    @wraps(func)  # 保持原函数的元信息
    def wrapper(*args, **kwargs):
        print("执行前...")
        result = func(*args, **kwargs)
        print("执行后...")
        return result
    return wrapper

@smart_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 输出：执行前... Hello, Alice! 执行后...
```

**`@wraps(func)` 的作用和重要性：**

`@wraps(func)` 是装饰器工厂，复制原函数的元信息到wrapper，避免调试时的混乱：

```python
from functools import wraps

# 对比：使用和不使用 @wraps 的区别
def decorator_without_wraps(func):
    def wrapper(*args, **kwargs):
        print("执行前...")
        return func(*args, **kwargs)
    return wrapper

def decorator_with_wraps(func):
    @wraps(func)  # 关键差别在这里
    def wrapper(*args, **kwargs):
        print("执行前...")
        return func(*args, **kwargs)
    return wrapper

# 测试两种装饰器
@decorator_without_wraps
def func1():
    """原始函数文档"""
    pass

@decorator_with_wraps
def func2():
    """原始函数文档"""
    pass

# 结果对比
print(func1.__name__)  # wrapper (身份丢失)
print(func1.__doc__)   # None (文档丢失)

print(func2.__name__)  # func2 (身份保持)
print(func2.__doc__)   # 原始函数文档 (文档保持)
```

**复制的关键属性：** `__name__`、`__doc__`、`__module__`、`__annotations__` 等

**结论：** `@wraps` 是可选的，装饰器功能不受影响，但强烈建议使用以保持代码的可调试性。

**装饰器参数传递的完整机制：**

```python
# 装饰器的本质：函数替换
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("装饰器逻辑")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add(x, y):
    return x + y

# 上面的 @my_decorator 等价于：
# add = my_decorator(add)
# 也就是说，现在的 add 实际上是 wrapper 函数

# 参数传递流程：
result = add(3, 5)
# 1. Python 调用 add(3, 5)，但 add 现在是 wrapper
# 2. wrapper(3, 5) 被执行，*args=(3,5), **kwargs={}
# 3. wrapper 内部调用原始函数 func(3, 5)
# 4. 返回结果
```

**关键理解：**
- 装饰器本质：`@decorator` 就是 `func = decorator(func)` 的语法糖
- **第一步**：`my_decorator(func)` 只接收原函数，返回 wrapper 函数
- **第二步**：`add = wrapper`，现在 add 指向 wrapper 函数
- **第三步**：调用 `add(3, 5)` 时，实际是调用 `wrapper(3, 5)`
- `*args, **kwargs`：让 wrapper 能接收调用时传入的任意参数
- `@wraps(func)`：纯粹的元信息复制工具，不影响参数传递
- 去掉 `@wraps` 后装饰器依然能正常工作，只是会丢失原函数的身份信息

**装饰器的两个阶段：**
```python
# 阶段1：装饰器定义时（只传func，没有*args/**kwargs）
def my_decorator(func):  # func 是原始的 add 函数
    def wrapper(*args, **kwargs):  # 这里定义了wrapper的参数接收能力
        print("装饰器逻辑")
        result = func(*args, **kwargs)  # 调用原函数
        return result
    return wrapper  # 返回新函数

# 阶段2：函数调用时（*args/**kwargs才发挥作用）
@my_decorator
def add(x, y):  # add = my_decorator(add) = wrapper
    return x + y

result = add(3, 5)  # 实际调用 wrapper(3, 5)，*args=(3,5)
```

**常用装饰器场景：**
- 缓存 (`@lru_cache`)
- 权限检查
- 重试逻辑
- 性能监控

## 5. AsyncIO — 异步并发编程 🧵

异步编程让I/O密集型任务并发执行，提高效率。

```python
import asyncio

async def fetch_data(name, delay):
    print(f"开始获取 {name}")
    await asyncio.sleep(delay)  # 模拟I/O等待
    print(f"{name} 数据获取完成")
    return f"{name}_data"

async def main():
    # 并发执行，而不是串行
    results = await asyncio.gather(
        fetch_data("用户信息", 1),
        fetch_data("订单数据", 2),
        fetch_data("商品列表", 1.5)
    )
    print(f"所有结果: {results}")

asyncio.run(main())
```

**运行结果：**
```
开始获取 用户信息
开始获取 订单数据
开始获取 商品列表
用户信息 数据获取完成
商品列表 数据获取完成
订单数据 数据获取完成
所有结果: ['用户信息_data', '订单数据_data', '商品列表_data']
```

**时间轴分析：**
- 0秒：三个任务同时开始
- 1秒：用户信息完成
- 1.5秒：商品列表完成
- 2秒：订单数据完成，所有任务结束
- **总耗时：约2秒**（而不是串行的4.5秒）

**核心概念：**
- `async def`：定义异步函数
- `await`：等待异步操作完成
- `asyncio.gather()`：并发执行多个任务
- 总执行时间约等于最长任务时间，而不是所有任务时间之和

**适用场景：**
- 网络请求
- 文件I/O
- 数据库操作
- WebSocket应用

## 6. 类型提示 — 代码的"安全网" 🔒

静态类型让Python代码更安全、可维护。

```python
from typing import TypedDict, Protocol
from dataclasses import dataclass

# TypedDict：字典结构类型化
class Person(TypedDict):
    name: str
    age: int

person: Person = {"name": "Alice", "age": 30}

# Protocol：定义接口
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("绘制圆形")

class Rectangle:
    def draw(self) -> None:
        print("绘制矩形")

def render(obj: Drawable) -> None:
    obj.draw()  # 只要有draw方法即可

# 使用
circle = Circle()
rect = Rectangle()
render(circle)  # 输出：绘制圆形
render(rect)    # 输出：绘制矩形

# dataclasses：自动生成类方法
@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)  # Point(x=1, y=2)
```

**核心工具：**
- `TypedDict`：为字典定义键值类型
- `Protocol`：定义接口约束
- `dataclasses`：减少样板代码
- `mypy/pyright`：静态类型检查器

**好处：**
- 更安全的重构
- 更好的IDE支持
- 自文档化
- 减少运行时错误

## 7. 总结

高阶Python语法让代码从"能用"变成"优雅"：

- **生成器**：内存友好的数据处理
- **描述符**：精确控制属性行为
- **元类**：定制类的创建过程
- **装饰器**：模块化功能增强
- **异步**：高效的并发处理
- **类型提示**：代码安全保障
