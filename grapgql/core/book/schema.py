from turtle import title
from unicodedata import category, name
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Answer, Question, Quizzes
# from .models import Books, Category, Answer, Question, Quizzes


# part1

# class Bookstype(DjangoObjectType):
#     class Meta:
#         model = Books
#         fields = ['id', 'title', 'excerpt']


# class Query(graphene.ObjectType):

#     all_books = graphene.List(Bookstype)

#     def resolve_all_books(root, info):
#         return Books.objects.filter(title='test')

# schema = graphene.Schema(query=Query)


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id', 'title', 'category')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz', 'date created', 'technique', 'difficulty', 'is_active')


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('answer_text', 'question', 'is_active')


class Query(graphene.ObjectType):
   
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    all_questions = DjangoListField(QuestionType)
    all_category = DjangoListField(CategoryType)
    all_answers = DjangoListField(AnswerType)


    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get(pk=id)

    def resolve_all_questions(root, info):
        return Question.objects.all()

    def resolve_all_category(root, info):
        return Category.objects.all()

    def resolve_all_answers(root, info):
        return Answer.objects.all()

# create new category (create operation)
class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info,name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)


class QuizMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        category = graphene.String()

    quiz = graphene.Field(QuizzesType)

    @classmethod
    def mutate(cls, root, info,title, id, category):
        quiz = Quizzes.objects.get(pk=id)
        quiz.title = title
        quiz.category = category
        category.save()
        return QuizMutation(quiz=quiz)


# update operation

class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.delete()
        return CategoryMutation(category=category)


# DELETE OPERATION

class CategoryDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return CategoryMutation(category=category)

class Mutetion(graphene.ObjectType):
    create_category = CategoryMutation.Field()
    update_category = CategoryMutation.Field()
    update_quiz = QuizMutation.Field()
    delete_category = CategoryDeleteMutation.Field()

schema = graphene.Schema(query=Query, mutation= Mutetion)