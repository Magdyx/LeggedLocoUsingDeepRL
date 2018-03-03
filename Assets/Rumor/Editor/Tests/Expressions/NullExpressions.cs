﻿#if UNITY_EDITOR

using Exodrifter.Rumor.Engine;
using Exodrifter.Rumor.Expressions;
using NUnit.Framework;
using System;

namespace Exodrifter.Rumor.Test.Expressions
{
	/// <summary>
	/// Ensure expressions work as expected when provided null values.
	/// </summary>
	public class NullExpressionsTest
	{
		/// <summary>
		/// Tests operations with null and bool values.
		/// </summary>
		[Test]
		public void NullAndBool()
		{
			var scope = new Scope();
			var bindings = new Bindings();
			scope.SetVar("a", true);

			Expression exp = new AddExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());
			exp = new AddExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());

			exp = new SubtractExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());
			exp = new SubtractExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());

			exp = new MultiplyExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());
			exp = new MultiplyExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());

			exp = new DivideExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());
			exp = new DivideExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());

			exp = new BoolAndExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolAndExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());

			exp = new BoolOrExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolOrExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
		}

		/// <summary>
		/// Tests operations with null and int values.
		/// </summary>
		[Test]
		public void NullAndInt()
		{
			var scope = new Scope();
			var bindings = new Bindings();
			scope.SetVar("a", 1);

			Expression exp = new AddExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(1, exp.Evaluate(scope, bindings).AsInt());
			exp = new AddExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(1, exp.Evaluate(scope, bindings).AsInt());

			exp = new SubtractExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(1, exp.Evaluate(scope, bindings).AsInt());
			exp = new SubtractExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(-1, exp.Evaluate(scope, bindings).AsInt());

			exp = new MultiplyExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(0, exp.Evaluate(scope, bindings).AsInt());
			exp = new MultiplyExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(0, exp.Evaluate(scope, bindings).AsInt());

			exp = new DivideExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(0, exp.Evaluate(scope, bindings).AsInt());
			exp = new DivideExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(0, exp.Evaluate(scope, bindings).AsInt());

			exp = new BoolAndExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolAndExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());

			exp = new BoolOrExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolOrExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
		}

		/// <summary>
		/// Tests operations with null and float values.
		/// </summary>
		[Test]
		public void NullAndFloat()
		{
			var scope = new Scope();
			var bindings = new Bindings();
			scope.SetVar("a", 1f);

			Expression exp = new AddExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(1f, exp.Evaluate(scope, bindings).AsFloat());
			exp = new AddExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(1f, exp.Evaluate(scope, bindings).AsFloat());

			exp = new SubtractExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(1f, exp.Evaluate(scope, bindings).AsFloat());
			exp = new SubtractExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(-1f, exp.Evaluate(scope, bindings).AsFloat());

			exp = new MultiplyExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(0f, exp.Evaluate(scope, bindings).AsFloat());
			exp = new MultiplyExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(0f, exp.Evaluate(scope, bindings).AsFloat());

			exp = new DivideExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(0f, exp.Evaluate(scope, bindings).AsFloat());
			exp = new DivideExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(0f, exp.Evaluate(scope, bindings).AsFloat());

			exp = new BoolAndExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolAndExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());

			exp = new BoolOrExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolOrExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
		}

		/// <summary>
		/// Tests operations with null and string values.
		/// </summary>
		[Test]
		public void NullAndString()
		{
			var scope = new Scope();
			var bindings = new Bindings();
			scope.SetVar("a", "1");

			Expression exp = new AddExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual("1", exp.Evaluate(scope, bindings).AsString());
			exp = new AddExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual("1", exp.Evaluate(scope, bindings).AsString());

			exp = new SubtractExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());
			exp = new SubtractExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());

			exp = new MultiplyExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());
			exp = new MultiplyExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());

			exp = new DivideExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());
			exp = new DivideExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.Throws<InvalidOperationException>(
				() => exp.Evaluate(scope, bindings).AsString());

			exp = new BoolAndExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolAndExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(false, exp.Evaluate(scope, bindings).AsBool());

			exp = new BoolOrExpression(
				new VariableExpression("a"),
				new VariableExpression("b")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
			exp = new BoolOrExpression(
				new VariableExpression("b"),
				new VariableExpression("a")
			);
			Assert.AreEqual(true, exp.Evaluate(scope, bindings).AsBool());
		}
	}
}

#endif
