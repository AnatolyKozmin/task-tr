"""Скрипт для создания проектника с дефолтными данными (для теста)"""
import asyncio
from database import get_session
from database.models import User, UserRoleEnum
from dao.user_dao import UserDAO
from utils.auth import get_password_hash


async def create_project_manager_default():
    """Создать проектника с дефолтными данными"""
    async with get_session() as session:
        # Проверяем, есть ли уже проектник
        existing = await UserDAO.get_by_role(session, UserRoleEnum.PROJECT_MANAGER)
        if existing:
            print("Проектник уже существует!")
            print("Для просмотра пользователей запустите: python check_users.py")
            return
        
        # Дефолтные данные для теста
        login = "admin"
        password = "admin123"
        full_name = "Проектник (Администратор)"
        
        print(f"Создание проектника с дефолтными данными:")
        print(f"  Логин: {login}")
        print(f"  Пароль: {password}")
        print(f"  Имя: {full_name}")
        
        project_manager = User(
            login=login,
            password_hash=get_password_hash(password),
            full_name=full_name,
            role=UserRoleEnum.PROJECT_MANAGER,
            is_admin=True
        )
        
        created = await UserDAO.create(session, project_manager)
        print(f"\n✅ Проектник успешно создан!")
        print(f"   ID: {created.id}")
        print(f"   Логин: {created.login}")
        print(f"   Пароль: {password}")
        print(f"\n⚠️  ВНИМАНИЕ: Это тестовые данные! Измените пароль в продакшене!")


if __name__ == "__main__":
    asyncio.run(create_project_manager_default())
