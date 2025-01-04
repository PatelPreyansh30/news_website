from base import db
from base.com.vo import UserVO, NewsVO

class UserDAO:
    def insert(self, vo_obj):
        db.session.add(vo_obj)
        db.session.commit()

    def get_user(self, email):
        return UserVO.query.filter_by(email=email).first()
        
    def match_user(self, email, password):
        return UserVO.query.filter_by(email=email, password=password).first()
        
    # def view(self):
    #     data = UserVO.query.all()
    #     return data

    # def delete(self, vo_obj):
    #     category_vo_obj = CategoryVO.query.get(category_vo.category_id)
    #     db.session.delete(category_vo_obj)
    #     db.session.commit()

    # def edit_category(self, category_vo):
    #     category_vo_obj = CategoryVO.query.filter_by(category_id = category_vo.category_id).first()
    #     return category_vo_obj

    # def update_category(self, category_vo):
    #     db.session.merge(category_vo)
    #     db.session.commit()

    # def order_by_category(self, category_vo):
    #     category_vo_obj = CategoryVO.query.order_by(asc(category_vo.category_name))
    #     return category_vo_obj
    
    
class NewsDAO:
    def insert(self, vo_obj):
        db.session.add(vo_obj)
        db.session.commit()
        
    def view(self):
        return NewsVO.query.all()